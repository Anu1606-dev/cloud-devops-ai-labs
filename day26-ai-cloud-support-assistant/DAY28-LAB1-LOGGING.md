# Day 28 — Lab 1: Structured Application Logging

## Objective

Implement structured application logging to make API requests observable and easier to troubleshoot.

## Implementation

The Express application now uses a centralized `logEvent()` helper to emit JSON log entries.

Each HTTP request receives a unique request ID generated with Node.js `crypto.randomUUID()`.

The request middleware records an event when the response finishes.

## Logged fields

| Field | Description |
|---|---|
| timestamp | Time when the event was recorded |
| level | Log severity: info, warn, or error |
| event | Event name |
| request_id | Unique identifier for the request |
| method | HTTP method |
| path | Requested API path |
| status | HTTP response status |
| duration_ms | Request processing duration |

Additional application events include application startup, RAG backend failures, invalid backend responses, and unexpected API errors.

## Log severity

- INFO: Successful requests and application events.
- WARN: Client-side HTTP errors.
- ERROR: Server-side failures.

## Validation evidence

- `node --check src/server.js` completed successfully.
- Docker image `cloud-support-assistant:day28` built successfully.
- Container `cloud-support-assistant-day28` started and reported healthy.
- `GET /health` returned HTTP 200.
- The response included request ID:
  `e8691f27-d805-4e04-bc2f-5e63c6d29905`
- Docker logs contained the matching `http_request` event:
  - Method: GET
  - Path: /health
  - Status: 200
  - Duration: 1 ms

The request was tested from inside the container using `docker exec`.

## Operational considerations

- Logs are written to standard output and collected through Docker logs.
- No external log aggregation platform or persistent log storage is configured.
- Health-check requests also generate log entries.
- Request bodies, user prompts, and secrets are not included in the HTTP request log.
- A separate Node.js process was listening on WSL localhost port 3000 during testing. Therefore, host-side localhost requests were not used as proof of container logging. The container was verified directly using `docker exec`.

## Limitations

This lab implements basic structured logging and request correlation. It does not yet provide centralized log aggregation, retention policies, alerting, or distributed tracing.

## Interview takeaway

Structured logging records application events in a consistent machine-readable format. A request ID helps correlate a client request with backend logs, while status codes and request duration help identify failures and latency problems.
