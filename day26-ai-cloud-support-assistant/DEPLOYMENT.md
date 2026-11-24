# Day 27 — Docker Deployment Guide

## 1. Architecture

The application runs as a single Docker container containing:

- Node.js 26 runtime
- Express API and frontend
- Python 3.11 virtual environment
- FastEmbed 0.9.1
- NumPy 2.4.6
- Day 25 RAG pipeline
- Day 24 knowledge-base chunks

Request flow:

Browser
  |
  v
Docker published port 3000
  |
  v
Express frontend and API
  |
  v
Python RAG service
  |
  v
FastEmbed semantic retrieval
  |
  v
Day 24 knowledge-base chunks
  |
  v
Mock response generator

## 2. Build the image

Run from the repository root:

    docker build \
      -f day26-ai-cloud-support-assistant/Dockerfile \
      -t cloud-support-assistant:day27 \
      .

## 3. Create persistent model storage

    docker volume create cloud-support-fastembed-cache

The named volume is intended to preserve the embedding-model cache
between container recreations.

## 4. Start the container

    docker run -d \
      --name cloud-support-assistant-day27 \
      -p 3000:3000 \
      -v cloud-support-fastembed-cache:/app/.cache/fastembed \
      cloud-support-assistant:day27

Open:

    http://localhost:3000

Health endpoint:

    http://localhost:3000/health

## 5. Environment configuration

| Variable | Purpose | Container default |
|---|---|---|
| PORT | HTTP listening port | 3000 |
| HOST | Server bind address | 0.0.0.0 |
| PYTHON_PATH | Python interpreter | /opt/venv/bin/python |
| FASTEMBED_CACHE_PATH | Embedding model cache location | /app/.cache/fastembed |

Do not place API keys or passwords in the Dockerfile or image.
Supply secrets at runtime through an appropriate secret-management
mechanism when real external services are introduced.

## 6. Runtime verification

    docker ps
    docker logs --tail 100 cloud-support-assistant-day27
    docker stats --no-stream cloud-support-assistant-day27

Inspect health status:

    docker inspect cloud-support-assistant-day27 \
      --format '{{.State.Health.Status}}'

## 7. Stop and remove the container

    docker stop cloud-support-assistant-day27
    docker rm cloud-support-assistant-day27

The named model-cache volume is retained unless explicitly removed.

## 8. Security and operational controls

- Application runs as the non-root node user.
- Express JSON request body is limited to 10 KB.
- Query input is validated and limited to 500 characters.
- API rate limit is 10 requests per minute.
- Docker publishes port 3000.
- Docker health check monitors /health.
- Model cache uses a named volume.
- No credentials are baked into the image.

## 9. Known limitations

- This is a local Docker deployment, not a public cloud deployment.
- The response generator is deterministic mock logic.
- No real LLM inference or Bedrock API call occurs.
- No TLS termination, reverse proxy, persistent application database,
  centralized logging, or external monitoring is configured.
- The first semantic retrieval may download the embedding model.

## 10. Deployment evidence

Image: cloud-support-assistant:day27
Docker daemon: 29.9.3
Node.js: 26.13.1
Python in container: 3.11.2
FastEmbed: 0.9.1
NumPy: 2.4.6

Verified:
- Container startup
- GET /health returns HTTP 200
- Frontend returns HTTP 200
- POST /api/rag returns HTTP 200
- Empty query returns HTTP 400
- Oversized JSON request returns HTTP 413
- Semantic retrieval returns source documents
