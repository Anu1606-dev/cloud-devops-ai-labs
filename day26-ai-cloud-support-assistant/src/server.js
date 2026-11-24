require("dotenv").config();

const express = require("express");

const app = express();
const PORT = process.env.PORT || 3000;

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

app.listen(PORT, "127.0.0.1", () => {
  console.log(`Assistant API running on http://127.0.0.1:${PORT}`);
});
