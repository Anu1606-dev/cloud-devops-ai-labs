# Day 28 — Lab 2: Application Metrics and Latency Monitoring

## Objective
Expose basic application-level operational metrics through an HTTP endpoint.

## Implementation
Added an in-memory metrics store and `GET /metrics` endpoint to `src/server.js`.

The endpoint reports:
- Application start timestamp
- Process uptime in seconds
- Total HTTP requests
- HTTP status counts: 2xx, 3xx, 4xx and 5xx
- Total, average and maximum request duration in milliseconds

## Measurement logic
The request-logging middleware measures request duration when the response finishes. It updates the counters according to the final HTTP status code.

Requests to `/metrics` are excluded from the counters to prevent the monitoring endpoint from counting itself.

## Validation
The updated Docker image was built as `cloud-support-assistant:day28`.
The container `cloud-support-assistant-day28` became healthy.

Test traffic:
- `GET /health` — HTTP 200
- `GET /` — HTTP 200
- `GET /missing-lab2-validation-route` — HTTP 404
- `GET /metrics` — HTTP 200 with JSON

A baseline-and-delta test checks that three test requests increment the total by three, two successful responses increment the 2xx counter by two, and one missing route increments the 4xx counter by one.

Repeated calls to `/metrics` do not change the request counters.

Docker health-check requests may also appear in the counters because they call `/health`.

## Limitations
- Metrics are stored in application memory and reset when the process restarts.
- Metrics are local to one application process/container.
- No historical storage, dashboard, alerting, or Prometheus integration is implemented.
- These metrics are suitable for this learning lab, not a complete production observability platform.

## Interview takeaway
Application metrics provide quantitative operational signals. Request counters show traffic and HTTP failure distribution, while latency measurements help identify performance degradation. Production systems generally export metrics to a monitoring backend for aggregation, dashboards and alerting.
