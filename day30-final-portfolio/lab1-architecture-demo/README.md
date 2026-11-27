# Day 30 — Lab 1: AI Cloud Support Assistant Architecture

## 1. Project Overview

The AI Cloud Support Assistant is a cloud-support troubleshooting
application that retrieves relevant technical guidance from a
knowledge base.

It combines:
- Node.js and Express for the application API.
- Python for the retrieval pipeline.
- FastEmbed for generating text embeddings.
- Vector-based semantic retrieval over prepared knowledge chunks.
- Docker for containerization.
- Structured logging, metrics, health checks and security controls.

The current assistant response adapter is a mock implementation.
The project demonstrates a retrieval-based support workflow; it
does not claim to run live LLM inference.

## 2. Architecture

```text
                    User
                     |
                     v
              Web Application
                     |
                     v
              Node.js / Express
                     |
          +----------+-----------+
          |          |           |
          v          v           v
        /health    /ready      /metrics
          |
          v
       RAG API
          |
          v
       Python RAG Service
          |
          v
       FastEmbed
          |
          v
   Query Embedding Generation
          |
          v
   Semantic Retrieval
          |
          v
   Knowledge Base Chunks
          |
          v
   Retrieved Sources
          |
          v
   Mock Response Adapter
          |
          v
       User Response

## 3. Technology Stack

| Area | Technology |
|---|---|
| Backend | Node.js, Express |
| Retrieval service | Python |
| Embeddings | FastEmbed |
| Retrieval | Semantic search |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Infrastructure as Code | Terraform |
| Logging | Structured JSON logs |
| Monitoring | Metrics and health endpoints |
| Security | Input screening and sensitive-data redaction |
| Version control | Git and GitHub |

## 4. Main Components

### Node.js / Express
- Exposes application endpoints.
- Handles incoming user requests.
- Connects the frontend with the retrieval service.
- Applies request-rate limiting.
- Provides health, readiness and metrics endpoints.

### Python RAG Service
- Receives the user's query.
- Uses FastEmbed to generate query embeddings.
- Searches prepared knowledge chunks.
- Returns relevant sources and similarity scores.

### Retrieval-Augmented Generation (RAG)

RAG retrieves relevant external knowledge before generating
or constructing an answer. This project demonstrates the
retrieval stage and currently uses a mock response adapter.

### Docker
- Packages the application and runtime dependencies.
- Uses a non-root application user.
- Includes a container health check.
- Uses a named volume for the embedding model cache.

### Observability and Security
- Structured application logs and request IDs.
- Health and readiness checks.
- Request metrics and failure counters.
- Prompt-injection screening.
- Sensitive-data redaction.

## 5. Infrastructure and DevOps Learning

The 30-day repository includes practical labs covering:

- Linux administration and system services.
- Networking fundamentals.
- AWS concepts and local simulations.
- Docker and Docker Compose.
- GitHub Actions CI/CD.
- Terraform and Infrastructure as Code.
- Monitoring, logging and troubleshooting.

Important: Day 29 used Terraform's local provider to practise
resource creation, state management, drift detection and cleanup.
It did not provision real AWS infrastructure.

## 6. Request Lifecycle

1. A user submits a troubleshooting question.
2. Express receives and validates the request.
3. The request is forwarded to the Python retrieval service.
4. FastEmbed converts the query into an embedding.
5. The retrieval pipeline searches the knowledge chunks.
6. Relevant sources and similarity scores are returned.
7. The mock response adapter constructs the response.
8. The application returns the response to the user.

## 7. Current Limitations

- No live LLM inference is enabled.
- No production AWS deployment is claimed.
- The knowledge base uses prepared local content.
- This is a portfolio and learning implementation,
  not a production-ready managed cloud service.

## 8. Future Improvements

- Integrate a live LLM through Amazon Bedrock or another provider.
- Deploy the application to AWS.
- Store documents in Amazon S3.
- Use a managed vector database.
- Add authentication and role-based access control.
- Add centralized monitoring and alerting.
- Introduce automated deployment pipelines.

## 9. Interview Summary

"I built a cloud-support assistant using Node.js, Express and
Python. The application uses a retrieval pipeline with FastEmbed
to find relevant troubleshooting knowledge from prepared
documents. I containerized the service with Docker and added
health checks, structured logging, metrics and security controls.

I also practised CI/CD using GitHub Actions and Infrastructure
as Code using Terraform. The current response adapter is mocked,
so I describe this as a RAG retrieval and cloud-operations
portfolio project rather than claiming a live LLM deployment."

## 10. Verification

The project should be validated through:

- Application health and readiness checks.
- RAG retrieval tests.
- Security unit tests.
- Docker container health checks.
- Metrics endpoint checks.
- Terraform validation and state-management exercises.
