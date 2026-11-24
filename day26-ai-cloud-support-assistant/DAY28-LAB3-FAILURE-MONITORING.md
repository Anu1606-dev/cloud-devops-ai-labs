# Day 28 — Lab 3: Failure Monitoring and Operational Checks

## Objective
Improve application failure visibility and distinguish process health from dependency readiness.

## 1. Readiness endpoint

Added `GET /ready`.

It checks:
- Whether the configured Python executable exists and has execute permission.
- Whether the configured RAG script exists and is readable.

Responses:
- HTTP 200: required paths are accessible.
- HTTP 503: one or more required paths are unavailable.

This is a lightweight filesystem readiness check. It does not execute a RAG request or verify every Python dependency.

## 2. Failure counters

Extended `GET /metrics` with:
- `rag_backend`: RAG subprocess execution failures.
- `invalid_backend_response`: invalid JSON returned by the RAG subprocess.
- `unexpected_api`: unexpected errors handled by Express middleware.

Counters are process-local and reset after application restart.

## 3. Structured failure events

Existing structured logs capture:
- `rag_backend_failure`
- `rag_invalid_response`
- `unexpected_api_error`
- `http_request`

Failure events include request IDs and relevant error metadata. The API returns generic error messages instead of exposing internal paths or stack traces.

## 4. Validation evidence

Normal container:
- `/health` returned HTTP 200.
- `/ready` returned HTTP 200.
- `/metrics` returned HTTP 200.
- Python runtime and RAG script were both reported available.
- Docker container remained healthy.

Controlled failure test:
- Started a separate test container with `PYTHON_PATH=/missing/python`.
- `/ready` returned HTTP 503 and reported the Python runtime unavailable.
- `POST /api/rag` returned HTTP 502.
- Failure counter `rag_backend` increased to 1.
- Structured logs recorded `rag_backend_failure` with error code `ENOENT`.
- The normal application container remained healthy.

## 5. Operational concepts

- **Liveness:** checks whether the application process responds.
- **Readiness:** checks whether required components are available to serve work.
- **Failure counter:** tracks the number of observed failures during the current process lifetime.
- **Structured logging:** records machine-readable events with consistent fields.
- **HTTP 502:** indicates that the API could not obtain a valid response from its upstream RAG process.
- **HTTP 503:** indicates that the service is not ready to handle work.

## 6. Limitations

- Metrics and failure counters are in-memory, not persistent.
- No external monitoring platform, alerting, or historical metrics storage is configured.
- Readiness checks file accessibility, not full RAG inference.
- The controlled failure test used a deliberately invalid Python executable in an isolated container.

## Interview takeaway

"I added a readiness endpoint separate from the liveness health check, instrumented application failure counters, and validated failure handling by simulating an unavailable Python backend. The API returned HTTP 502, readiness returned HTTP 503, and structured logs captured the failure with a request ID."
