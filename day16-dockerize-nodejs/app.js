const express = require("express");

const app = express();

const PORT = process.env.PORT || 3000;

app.get("/", (req, res) => {
    res.send("Hello from my Dockerized Node.js application!");
});

app.get("/health", (req, res) => {
    res.json({
        status: "healthy",
        application: "day16-docker-nodejs"
    });
});

app.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on port ${PORT}`);
});
