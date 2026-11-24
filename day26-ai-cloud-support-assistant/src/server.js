
require("dotenv").config();

const express = require("express");
const path = require("node:path");
const { execFile } = require("node:child_process");

const app = express();
const PORT = process.env.PORT || 3000;

const PYTHON_PATH =
  process.env.PYTHON_PATH ||
  path.resolve(
    __dirname,
    "../../day22-bedrock-apis/.venv/bin/python"
  );

const RAG_SCRIPT = path.join(__dirname, "rag_service.py");

app.use(express.json());

app.get("/", (req, res) => {
  res.status(200).json({
    message: "AI Cloud Support Assistant API",
    status: "running",
  });
});

app.get("/health", (req, res) => {
  res.status(200).json({
    status: "healthy",
    service: "ai-cloud-support-assistant",
  });
});

// Connect the Express API to the Python RAG pipeline.
app.post("/api/rag", (req, res) => {
  const query = req.body?.query;

  if (typeof query !== "string" || !query.trim()) {
    return res.status(400).json({
      error: "A non-empty query is required.",
    });
  }

  execFile(
    PYTHON_PATH,
    [RAG_SCRIPT, query.trim()],
    {
      timeout: 60000,
      maxBuffer: 1024 * 1024,
    },
    (error, stdout, stderr) => {
      if (error) {
        console.error("RAG execution failed:", error.message, stderr);

        return res.status(500).json({
          error: "RAG retrieval failed. Check server logs.",
        });
      }

      try {
        const ragResult = JSON.parse(stdout);

        return res.status(200).json({
          status: "success",
          ...ragResult,
        });
      } catch (parseError) {
        console.error("Invalid RAG JSON response:", parseError.message);

        return res.status(500).json({
          error: "Invalid response from RAG service.",
        });
      }
    }
  );
});

app.listen(PORT, "127.0.0.1", () => {
  console.log(`Assistant API running on http://127.0.0.1:${PORT}`);
});
