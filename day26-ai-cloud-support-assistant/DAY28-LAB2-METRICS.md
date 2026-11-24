# Day 28 — Lab 2: Metrics and Latency Monitoring

## Objective

Expose basic application traffic and latency measurements through an HTTP metrics endpoint.

## Implementation

The Express application maintains in-memory counters and exposes them through `GET /metrics`.

### Request metrics
- Total HTTP requests
- 2xx successful responses
- 3xx redirects
- 4xx client errors
- 5xx server errors

### Latency metrics
- Average request duration in milliseconds
- Maximum observed request duration
- Total accumulated request duration

### Runtime metrics
- Application start timestamp
- Process uptime in seconds

## Design decisions

- Metrics are maintained in application memory.
- The `/metrics` endpoint is excluded from request counters to prevent self-observation.
- Counters reset when the application restarts.
- No external monitoring service is required.

## Limitations

These are basic process-local metrics, not production-grade distributed metrics. They are not persisted, aggregated across replicas, or exported in Prometheus format.

## Interview takeaway

Application metrics provide quantitative visibility into traffic, error rates, and latency. Request counts reveal traffic volume, status-code distributions help identify failures, and latency measurements help detect performance degradation.
