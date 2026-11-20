
# Day 20 — Docker CI Automation 🚀

## Overview

This lab implements a Docker-focused Continuous Integration (CI) pipeline using GitHub Actions.

The pipeline automatically checks the Docker environment, validates the Docker Compose configuration, and builds a Node.js application image whenever code is pushed to the `main` branch or a pull request is opened.

## Objectives

- Automate Docker environment verification
- Validate Docker Compose configuration in CI
- Build a Node.js Docker image automatically
- Understand CI failure detection and troubleshooting
- Simulate a Docker build failure and recover from it
- Practice Git-based workflow updates and verification

## CI Pipeline Architecture

```text
Developer Push / Pull Request
          |
          v
    GitHub Actions
          |
          v
  Checkout Repository
          |
          v
 Check Docker Version
          |
          v
 Check Docker Compose Version
          |
          v
 Prepare .env File
          |
          v
 Validate Compose Configuration
          |
          v
 Build Node.js Docker Image
          |
          v
    Pipeline Result
    /           \
 Success       Failure
```

## Workflow Configuration

Workflow file:

`.github/workflows/day20-docker-ci.yml`

### Pipeline triggers

- `push` to the `main` branch
- `pull_request` events

### CI steps

| Step | Purpose |
|---|---|
| Checkout repository | Downloads repository contents to the runner |
| Docker version check | Verifies Docker CLI availability |
| Docker Compose check | Verifies Docker Compose availability |
| Prepare environment | Copies `.env.example` to `.env` |
| Compose validation | Checks Compose configuration syntax and validity |
| Docker image build | Builds the Node.js application image |
| Display success | Prints a success message when previous steps pass |

## Docker Image Build

The CI pipeline builds the Node.js application using:

```bash
docker build -t day20-day17-app:ci ./day17-docker-compose
```

### Command breakdown

- `docker build` — builds an image from a Dockerfile
- `-t` — assigns a name and tag to the image
- `day20-day17-app` — image name
- `ci` — image tag
- `./day17-docker-compose` — Docker build context

The image is built inside the GitHub Actions runner. This pipeline does not push the image to Docker Hub or another container registry.

## Docker Compose Validation

Before building the application image, CI prepares the environment file:

```bash
cp day17-docker-compose/.env.example day17-docker-compose/.env
```

Then validates the Compose configuration:

```bash
docker compose -f compose.yaml config --quiet
```

This helps detect configuration problems before deployment.

## Failure Simulation & Troubleshooting

### Intentional failure

A missing Dockerfile was referenced to simulate a pipeline failure:

```bash
docker build -t day20-day17-app:ci \
  -f day17-docker-compose/Dockerfile.missing \
  ./day17-docker-compose
```

### Expected result

The Docker build fails because the specified Dockerfile does not exist.

The GitHub Actions job reports failure and stops subsequent steps.

### Root cause

Incorrect Dockerfile path:

`day17-docker-compose/Dockerfile.missing`

### Resolution

Restored the correct Docker build command:

```bash
docker build -t day20-day17-app:ci ./day17-docker-compose
```

The change was pushed to GitHub, and the pipeline was verified green.

## Troubleshooting Approach

1. Identify the failed workflow run.
2. Locate the failed job and step.
3. Review the available error logs.
4. Identify the root cause.
5. Correct the configuration or command.
6. Commit and push the fix.
7. Verify the workflow succeeds.

## Git Workflow

Check the repository state:

```bash
git status
```

Review changes:

```bash
git diff --check
git diff
```

Commit changes:

```bash
git add .
git commit -m "Document Day 20 Docker CI automation"
git push origin main
```

## Key Concepts Learned

- Continuous Integration (CI)
- GitHub Actions workflows
- Workflow triggers
- Jobs and steps
- Docker build context
- Docker image tagging
- Docker Compose validation
- Environment file preparation
- CI failure detection
- Root cause analysis
- Failure recovery
- Git-based automation

## Interview Questions

### 1. What is Continuous Integration?

Continuous Integration is the practice of automatically validating code changes through a pipeline whenever developers integrate or submit code.

### 2. What is GitHub Actions?

GitHub Actions is a CI/CD automation platform used to run workflows triggered by repository events.

### 3. What is the difference between a Docker image and a container?

A Docker image is a packaged template containing an application's filesystem and configuration. A container is a running or created instance of that image.

### 4. Why validate Docker Compose configuration in CI?

It helps detect configuration errors before the application is deployed or executed in an environment.

### 5. What happens if a CI step fails?

The step returns a non-zero exit code. GitHub Actions marks the job as failed and normally skips subsequent steps.

### 6. Does this pipeline deploy the application?

No. It validates the configuration and builds the Docker image. It does not deploy the application or push the image to a registry.

### 7. How do you troubleshoot a failed pipeline?

Identify the failed step, examine the logs, isolate the cause, fix the configuration or command, push the correction, and verify the new run.

## Lab Results

- Docker environment checks completed
- Docker Compose configuration validation automated
- Node.js Docker image build automated
- CI failure intentionally simulated
- Incorrect Dockerfile path corrected
- Successful pipeline recovery verified
- Changes version-controlled and pushed to GitHub

## Conclusion

This lab demonstrates a basic Docker CI pipeline using GitHub Actions. It automates environment checks, Compose validation, and Docker image building, while also practicing failure simulation and troubleshooting.

**Status: Completed ✅**
