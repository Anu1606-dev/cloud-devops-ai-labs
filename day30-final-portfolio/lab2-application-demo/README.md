# Day 30 — Lab 2: End-to-End Application Demo

## 1. Objective

Validate the Cloud Support Assistant from its Docker container
through its HTTP endpoints and RAG retrieval workflow.

## 2. Docker Validation

- Image: cloud-support-assistant:day30
- Container: cloud-support-assistant-day27
- Host port: 3000
- Container port: 3000
- FastEmbed cache: cloud-support-fastembed-cache
- Container healthcheck: Docker HEALTHCHECK

## 3. API Validation

| Endpoint | Purpose |
|---|---|
| GET /health | Application health |
| GET /ready | Application readiness |
| GET /metrics | Application metrics |
| POST /api/rag | Knowledge retrieval and response |

## 4. Input Validation

Tested an empty RAG query to verify request validation.

## 5. Security Validation

Executed the Python security unit test suite.

Coverage includes:
- Prompt injection detection
- Instruction override detection
- Secret disclosure detection
- Retrieved instruction filtering
- AWS access key redaction
- Bearer token redaction
- JWT redaction
- Password and API key redaction
- Normal troubleshooting text handling

## 6. Code Validation

- Python compilation using py_compile
- Node.js syntax validation using node --check

## 7. AI and RAG Limitations

- The application uses prepared local knowledge-base content.
- FastEmbed performs local embedding-based retrieval.
- The response adapter is a mock implementation.
- No live LLM inference is performed.
- No production AWS deployment is claimed.

## 8. Result

Docker image cloud-support-assistant:day30 built successfully.
Container reached healthy status.

Observed HTTP results:
- GET /health: 200 OK
- GET /ready: 200 OK
- GET /metrics: 200 OK
- POST /api/rag: 200 OK
- Empty RAG query: 400 Bad Request

RAG retrieval returned three relevant knowledge-base documents.
The response explicitly identified the model as a mock adapter
with inference_performed=false.

Security tests: 12/12 passed.
Python compilation: passed.
Node.js syntax validation: passed.

The application was validated locally using Docker.
