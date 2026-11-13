const { handler } = require("./lambda-function");

const tests = [
    {
        label: "Health Check",
        event: {
            version: "2.0",
            rawPath: "/health",
            requestContext: {
                http: { method: "GET" }
            },
            body: null
        }
    },
    {
        label: "Valid Greeting",
        event: {
            version: "2.0",
            rawPath: "/greet",
            requestContext: {
                http: { method: "POST" }
            },
            body: JSON.stringify({ name: "Anushka" })
        }
    },
    {
        label: "Missing Name",
        event: {
            version: "2.0",
            rawPath: "/greet",
            requestContext: {
                http: { method: "POST" }
            },
            body: "{}"
        }
    },
    {
        label: "Unknown Route",
        event: {
            version: "2.0",
            rawPath: "/unknown",
            requestContext: {
                http: { method: "GET" }
            },
            body: null
        }
    }
];

async function runTests() {
    for (const test of tests) {
        const result = await handler(
            test.event,
            { awsRequestId: "local-test" }
        );

        console.log(`\n${test.label}: HTTP ${result.statusCode}`);
        console.log(JSON.parse(result.body));
    }
}

runTests().catch(error => {
    console.error("Test failed:", error);
    process.exitCode = 1;
});
