const express = require("express");
const { createClient } = require("redis");

const app = express();
const PORT = process.env.PORT || 3000;

const redisClient = createClient({
    url: process.env.REDIS_URL || "redis://redis:6379"
});

redisClient.on("error", (err) => {
    console.error("Redis error:", err.message);
});

async function connectRedis() {
    while (!redisClient.isOpen) {
        try {
            await redisClient.connect();
            console.log("Connected to Redis successfully!");
        } catch (error) {
            console.error("Redis connection failed. Retrying in 2 seconds...");
            await new Promise(resolve => setTimeout(resolve, 2000));
        }
    }
}

app.get("/", (req, res) => {
    res.json({
        message: "Day 17 Docker Compose application is running!",
        services: ["Node.js", "Redis"]
    });
});

app.get("/redis", async (req, res) => {
    try {
        const response = await redisClient.ping();
        res.json({
            redis: "connected",
            response
        });
    } catch (error) {
        res.status(503).json({
            redis: "unavailable",
            error: error.message
        });
    }
});

app.listen(PORT, "0.0.0.0", () => {
    console.log(`API running on port ${PORT}`);
    connectRedis();
});
