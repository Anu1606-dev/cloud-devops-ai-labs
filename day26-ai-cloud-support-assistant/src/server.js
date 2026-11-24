
require("dotenv").config();

const express = require("express");
const path = require("path");
const { execFile } = require("child_process");
const { rateLimit } = require("express-rate-limit");

const app = express();
const PORT = process.env.PORT || 3000;

// Limit incoming JSON request bodies to 10 KB.
app.use(express.json({ limit: "10kb" }));

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

// Protected RAG endpoint.
app.post("/api/rag", ragLimiter, (req, res) => {
  const query = req.body?.query;

  // Validate query type.
  if (typeof query !== "string") {
    return res.status(400).json({
      error: "Query must be a string."
    });
  }

  const trimmedQuery = query.trim();

  // Reject empty queries.
  if (!trimmedQuery) {
    return res.status(400).json({
      error: "A non-empty query is required."
    });
  }

  // Limit query length.
  if (trimmedQuery.length > 500) {
    return res.status(400).json({
      error: "Query must not exceed 500 characters."
    });
  }

  // Execute the Python RAG service without shell interpolation.
  execFile(
    PYTHON_PATH,
    [RAG_SCRIPT, trimmedQuery],
    {
      timeout: 60000,
      maxBuffer: 1024 * 1024
    },
    (error, stdout, stderr) => {
      if (error) {
        console.error("RAG backend execution failed:", error.message);

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
        console.error("Invalid RAG backend response.");

        return res.status(502).json({
          error: "Invalid response received from RAG backend."
        });
      }
    }
  );
});

// Centralized error handling middleware.
// This must be registered after routes.
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

  console.error("Unexpected API error:", error.message);

  return res.status(500).json({
    error: "Internal server error."
  });
});

// Start the API.
app.listen(PORT, "127.0.0.1", () => {
  console.log(
    `Assistant API running on http://127.0.0.1:${PORT}`
  );
});
