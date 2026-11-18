# Day 16 — Dockerize a Node.js Application

## Objective
Build a Docker image for an Express.js application and run it as a container.

## Technology
- Node.js 22 (Alpine)
- Express.js 5
- Docker Desktop
- Docker Buildx

## Application endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Returns a welcome message |
| `/health` | Returns application health as JSON |

## Dockerfile concepts

- `FROM`: Selects the Node.js Alpine base image.
- `WORKDIR`: Sets `/app` as the working directory.
- `COPY`: Copies dependency manifests and application source.
- `RUN`: Installs production dependencies using `npm ci --omit=dev`.
- `EXPOSE`: Documents container port 3000.
- `CMD`: Starts the Node.js application.

## Build and run

```bash
docker build --check .
docker build -t day16-node-app:1.0 .
docker run -d --name day16-node-app -p 8080:3000 day16-node-app:1.0
