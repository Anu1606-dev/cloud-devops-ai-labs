function apiResponse(statusCode, data) {
    return {
        statusCode,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    };
}

exports.handler = async (event, context) => {
    const method =
        event?.requestContext?.http?.method ||
        event?.httpMethod ||
        "GET";

    const path = event?.rawPath || event?.path || "/";

    if (method === "GET" && path === "/health") {
        return apiResponse(200, {
            status: "healthy",
            message: "Lambda function is running!"
        });
    }

    if (method === "POST" && path === "/greet") {
        let payload;

        try {
            payload = JSON.parse(event.body || "{}");
        } catch {
            return apiResponse(400, {
                error: "Invalid JSON request body"
            });
        }

        const name =
            typeof payload.name === "string"
                ? payload.name.trim()
                : "";

        if (!name) {
            return apiResponse(400, {
                error: "Name is required"
            });
        }

        return apiResponse(200, {
            message: `Hello, ${name}!`,
            source: "Lambda handler simulation"
        });
    }

    return apiResponse(404, {
        error: "Route not found"
    });
};
