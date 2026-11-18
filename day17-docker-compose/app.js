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
    while (!redisClient.isReady) {
        try {
            if (!redisClient.isOpen) {
                await redisClient.connect();
            } else {
                await new Promise(resolve => setTimeout(resolve, 1000));
            }
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

app.get("/health", (req, res) => {
    if (redisClient.isReady) {
        return res.status(200).json({
            status: "healthy",
            redis: "ready"
        });
    }

    return res.status(503).json({
        status: "unhealthy",
        redis: "not ready"
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
    console.log(`Environment: ${process.env.NODE_ENV || "development"}`);
    connectRedis();
});
