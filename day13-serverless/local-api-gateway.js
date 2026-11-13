const http = require("node:http");
const { handler } = require("./lambda-function");

const HOST = "127.0.0.1";
const PORT = 3001;

const server = http.createServer(async (req, res) => {
    try {
        let body = "";

        for await (const chunk of req) {
            body += chunk;
        }

        const pathname = new URL(
            req.url,
            `http://${HOST}:${PORT}`
        ).pathname;

        const event = {
            version: "2.0",
            rawPath: pathname,
            headers: req.headers,
            requestContext: {
                http: {
                    method: req.method,
                    path: pathname
                }
            },
            body: body || null,
            isBase64Encoded: false
        };

        const lambdaResult = await handler(event, {
            awsRequestId: "local-api-gateway"
        });

        res.writeHead(
            lambdaResult.statusCode,
            lambdaResult.headers
        );

        res.end(lambdaResult.body);
    } catch (error) {
        console.error("Gateway simulation error:", error);

        res.writeHead(502, {
            "Content-Type": "application/json"
        });

        res.end(JSON.stringify({
            error: "Internal server error"
        }));
    }
});

server.listen(PORT, HOST, () => {
    console.log(
        `Local API Gateway running at http://${HOST}:${PORT}`
    );
});
