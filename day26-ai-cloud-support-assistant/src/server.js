
require("dotenv").config();

const express = require("express");
const path = require("path");
const fs = require("fs");
const crypto = require("crypto");
const { execFile } = require("child_process");
const { rateLimit } = require("express-rate-limit");

const app = express();
const PORT = process.env.PORT || 3000;
const HOST = process.env.HOST || "0.0.0.0";

// Structured JSON logging.
function logEvent(level, event, details = {}) {
  console.log(JSON.stringify({
    timestamp: new Date().toISOString(),
    level,
    event,
    ...details
  }));
}

// Limit incoming JSON request bodies to 10 KB.
app.use(express.json({ limit: "10kb" }));

// In-memory metrics for this Node.js process.
// These counters reset whenever the application restarts.
const metrics = {
  startedAt: new Date().toISOString(),
  totalRequests: 0,
  status2xx: 0,
  status3xx: 0,
  status4xx: 0,
  status5xx: 0,
  totalDurationMs: 0,
  maxDurationMs: 0,
  ragBackendFailures: 0,
  ragInvalidResponses: 0,
  unexpectedApiErrors: 0
};

// Request logging middleware.
// Register before routes so all responses are observed.
app.use((req, res, next) => {
  const startTime = Date.now();

  req.requestId = crypto.randomUUID();
  res.setHeader("X-Request-ID", req.requestId);

  res.on("finish", () => {
    const durationMs = Date.now() - startTime;


    // Exclude /metrics requests to prevent self-counting.
    if (req.path !== "/metrics") {
      metrics.totalRequests += 1;
      metrics.totalDurationMs += durationMs;
      metrics.maxDurationMs = Math.max(metrics.maxDurationMs, durationMs);

      if (res.statusCode >= 200 && res.statusCode < 300) {
        metrics.status2xx += 1;
      } else if (res.statusCode >= 300 && res.statusCode < 400) {
        metrics.status3xx += 1;
      } else if (res.statusCode >= 400 && res.statusCode < 500) {
        metrics.status4xx += 1;
      } else if (res.statusCode >= 500) {
        metrics.status5xx += 1;
      }
    }
    const level =
      res.statusCode >= 500 ? "error" :
      res.statusCode >= 400 ? "warn" : "info";

    logEvent(level, "http_request", {
      request_id: req.requestId,
      method: req.method,
      path: req.path,
      status: res.statusCode,
      duration_ms: durationMs
    });
  });

  next();
});

// Serve frontend files.
app.use(express.static(path.join(__dirname, "../public")));

// Python environment and RAG service paths.
const PYTHON_PATH =
  process.env.PYTHON_PATH ||
  path.resolve(
    __dirname,
    "../../day22-bedrock-apis/.venv/bin/python"
  );

const RAG_SCRIPT = path.join(__dirname, "rag_service.py");

// Rate limiter: maximum 10 requests per IP per minute.
const ragLimiter = rateLimit({
  windowMs: 60 * 1000,
  limit: 10,
  standardHeaders: "draft-8",
  legacyHeaders: false,
  message: {
    error: "Too many requests. Please try again later."
  }
});

// Metrics endpoint. Its own requests are excluded from the counters.
app.get("/metrics", (req, res) => {
  const uptimeSeconds = process.uptime();
  const averageDurationMs = metrics.totalRequests
    ? Number((metrics.totalDurationMs / metrics.totalRequests).toFixed(2))
    : 0;

  res.status(200).json({
    started_at: metrics.startedAt,
    uptime_seconds: Number(uptimeSeconds.toFixed(2)),
    total_requests: metrics.totalRequests,
    status_counts: {
      "2xx": metrics.status2xx,
      "3xx": metrics.status3xx,
      "4xx": metrics.status4xx,
      "5xx": metrics.status5xx
    },
    failure_counts: {
      rag_backend: metrics.ragBackendFailures,
      invalid_backend_response: metrics.ragInvalidResponses,
      unexpected_api: metrics.unexpectedApiErrors
    },
    latency_ms: {
      total: metrics.totalDurationMs,
      average: averageDurationMs,
      maximum: metrics.maxDurationMs
    }
  });
});

// Root endpoint.
app.get("/", (req, res) => {
  res.status(200).json({
    message: "AI Cloud Support Assistant API",
    status: "running"
  });
});

// Health endpoint.
app.get("/health", (req, res) => {
  res.status(200).json({
    status: "healthy",
    service: "ai-cloud-support-assistant"
  });
});

// Readiness endpoint: checks required local RAG runtime components.
app.get("/ready", (req, res) => {
  let pythonAvailable = false;
  let ragScriptAvailable = false;

  try {
    fs.accessSync(PYTHON_PATH, fs.constants.X_OK);
    pythonAvailable = true;
  } catch {}

  try {
    fs.accessSync(RAG_SCRIPT, fs.constants.R_OK);
    ragScriptAvailable = true;
  } catch {}

  const ready = pythonAvailable && ragScriptAvailable;

  res.status(ready ? 200 : 503).json({
    status: ready ? "ready" : "not_ready",
    checks: {
      python_runtime: pythonAvailable ? "available" : "unavailable",
      rag_script: ragScriptAvailable ? "available" : "unavailable"
    }
  });
});

// Protected RAG endpoint.
app.post("/api/rag", ragLimiter, (req, res) => {
  const query = req.body?.query;

  if (typeof query !== "string") {
    return res.status(400).json({
      error: "Query must be a string."
    });
  }

  const trimmedQuery = query.trim();

  if (!trimmedQuery) {
    return res.status(400).json({
      error: "A non-empty query is required."
    });
  }

  if (trimmedQuery.length > 500) {
    return res.status(400).json({
      error: "Query must not exceed 500 characters."
    });
  }

  execFile(
    PYTHON_PATH,
    [RAG_SCRIPT, trimmedQuery],
    {
      timeout: 60000,
      maxBuffer: 1024 * 1024
    },
    (error, stdout, stderr) => {
      if (error) {
        metrics.ragBackendFailures += 1;
        logEvent("error", "rag_backend_failure", {
          request_id: req.requestId,
          error_name: error.name,
          error_code: error.code || "UNKNOWN"
        });

        if (error.killed || error.code === "ETIMEDOUT") {
          return res.status(504).json({
            error: "RAG backend request timed out."
          });
        }

        return res.status(502).json({
          error: "RAG backend is temporarily unavailable."
        });
      }

      try {
        const ragResult = JSON.parse(stdout);

        return res.status(200).json({
          status: "success",
          ...ragResult
        });
      } catch (parseError) {
        metrics.ragInvalidResponses += 1;
        logEvent("error", "rag_invalid_response", {
          request_id: req.requestId,
          error_name: parseError.name
        });

        return res.status(502).json({
          error: "Invalid response received from RAG backend."
        });
      }
    }
  );
});

// Centralized error handling middleware.
app.use((error, req, res, next) => {
  if (error.type === "entity.too.large") {
    return res.status(413).json({
      error: "Request body is too large. Maximum size is 10 KB."
    });
  }

  if (error instanceof SyntaxError && error.status === 400) {
    return res.status(400).json({
      error: "Invalid JSON request body."
    });
  }

  metrics.unexpectedApiErrors += 1;
  logEvent("error", "unexpected_api_error", {
    request_id: req.requestId || "unavailable",
    error_name: error.name || "Error"
  });

  return res.status(500).json({
    error: "Internal server error."
  });
});

// Start the API.
app.listen(PORT, HOST, () => {
  logEvent("info", "application_started", {
    host: HOST,
    port: PORT
  });
});

