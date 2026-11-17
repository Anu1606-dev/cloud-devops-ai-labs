# Day 15 — Docker Basics 🐳

## 🎯 Learning Objectives

- Understand containerization and Docker architecture.
- Differentiate Docker images and containers.
- Understand image layers, caching, and registries.
- Pull, inspect, run, and manage Docker containers.
- Access a container and inspect its resource usage.
- Practise the Docker container lifecycle.

## 🧠 1. Docker Fundamentals

### What is Docker?

Docker is a containerization platform that packages an application and its dependencies into a portable unit called a container.

It helps solve the "works on my machine" problem by providing a consistent runtime environment.

### Virtual Machines vs Containers

| Virtual Machines | Containers |
|---|---|
| Run a full guest OS | Share the host OS kernel |
| Require a hypervisor | Run through a container runtime |
| Generally heavier | Generally lightweight |
| Usually slower to start | Usually faster to start |

### Docker Architecture

- **Docker Client:** Accepts commands such as `docker run`.
- **Docker Daemon (`dockerd`):** Manages images, containers, networks, and volumes.
- **Docker Engine:** The platform that provides the Docker runtime and management functionality.
- **Docker Registry:** Stores and distributes Docker images. Docker Hub is a common public registry.

### Image vs Container

- **Image:** Read-only template containing application code, runtime, libraries, and dependencies.
- **Container:** An instance of an image with an isolated process environment and a writable container layer.

### Image Layers and Caching

Docker images consist of layers. Images can share common layers, reducing redundant storage.

Docker can reuse unchanged build layers from its cache, making subsequent image builds faster.

### Container Lifecycle

Created → Running → Stopped/Exited → Removed

A stopped container can be started again. Removing a container does not automatically remove its image.

## 🧰 2. Environment Setup

- Operating system: Windows with WSL2
- Linux distribution: Ubuntu-D
- Container platform: Docker Desktop
- Backend: WSL2
- Docker Engine: 29.9.3
- Docker Desktop: 4.99.0
- Image architecture: Linux AMD64

Docker Desktop WSL Integration was enabled for Ubuntu-D.

Verification commands:

```bash
docker --version
docker version
docker info
```

## 🧪 3. Practical Labs

### Lab 1 — Verify Docker Installation

```bash
docker --version
docker version
docker info
```

**Purpose:**
- Check Docker CLI installation.
- Verify both client and server connectivity.
- Inspect Docker Engine information.

### Lab 2 — Inspect Existing Images and Containers

```bash
docker images
docker ps -a
```

**Purpose:**
- `docker images`: Lists locally available images.
- `docker ps -a`: Lists all containers, including stopped containers.

### Lab 3 — Pull and Inspect Nginx

```bash
docker pull nginx:alpine
docker images
docker image inspect nginx:alpine
docker image ls nginx
```

**Result:**
- Successfully downloaded `nginx:alpine`.
- Image architecture: AMD64.
- Exposed container port: 80/tcp.
- Nginx version observed: 1.31.8.

### Lab 4 — Run an Nginx Container

```bash
docker run -d --name day15-nginx -p 8080:80 nginx:alpine
```

**Command breakdown:**

| Option | Meaning |
|---|---|
| `docker run` | Creates and starts a container |
| `-d` | Detached/background mode |
| `--name` | Assigns a container name |
| `-p 8080:80` | Maps host port 8080 to container port 80 |
| `nginx:alpine` | Image and tag |

Verify:

```bash
docker ps
curl -I http://localhost:8080
```

**Result:** Nginx returned `HTTP/1.1 200 OK` and the welcome page was accessible in the browser at:

`http://localhost:8080`

### Lab 5 — Inspect and Manage the Container

```bash
docker logs day15-nginx
docker inspect day15-nginx
docker inspect --format='{{.State.Status}}' day15-nginx
```

**Purpose:**
- `docker logs`: Displays container logs.
- `docker inspect`: Displays detailed container configuration and metadata.
- `--format`: Extracts a specific field from the inspection output.

Open a shell inside the running container:

```bash
docker exec -it day15-nginx sh
```

Inside the container:

```sh
hostname
pwd
ls
exit
```

Inspect resource usage:

```bash
docker stats --no-stream day15-nginx
```

**Observations:**
- Container status was `running`.
- Container used Docker's bridge network.
- Container IP observed: `172.17.0.2`.
- Host port 8080 mapped to container port 80.
- Container shell showed its isolated filesystem.
- Resource statistics were successfully displayed.

### Lab 6 — Container Lifecycle

Stop the container:

```bash
docker stop day15-nginx
docker ps
docker ps -a
```

Start the existing container:

```bash
docker start day15-nginx
docker ps
```

Restart it:

```bash
docker restart day15-nginx
docker ps
curl -I http://localhost:8080
```

Remove the container:

```bash
docker stop day15-nginx
docker rm day15-nginx
```

Verify:

```bash
docker ps -a
docker images
```

**Result:**
- Stop, start, and restart operations succeeded.
- Nginx continued returning HTTP 200 after restart.
- The container was successfully removed.
- The `nginx:alpine` image remained available locally.

## 🔍 4. Troubleshooting Notes

| Observation | Explanation |
|---|---|
| `favicon.ico` returned 404 | Browser requested a favicon that was not present; the main Nginx page still returned 200 |
| `hotname` command failed | Typo; correct command is `hostname` |
| `docker image ls niginx` returned no result | Typo; correct image name is `nginx` |

These were harmless command/input mistakes, not Docker Engine failures.

## 💡 5. Important Docker Commands

| Command | Purpose |
|---|---|
| `docker pull IMAGE` | Download an image |
| `docker images` | List local images |
| `docker image inspect IMAGE` | Inspect image details |
| `docker run` | Create and start a container |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker logs NAME` | View container logs |
| `docker inspect NAME` | Inspect container details |
| `docker exec -it NAME sh` | Open a shell inside a running container |
| `docker stats` | View resource usage |
| `docker stop NAME` | Stop a container |
| `docker start NAME` | Start an existing container |
| `docker restart NAME` | Restart a container |
| `docker rm NAME` | Remove a container |
| `docker rmi IMAGE` | Remove an image |

## 🎤 6. Interview Preparation

**Q1. What is Docker?**

Docker is a containerization platform that packages applications and their dependencies into portable containers.

**Q2. What is the difference between an image and a container?**

An image is a read-only template, while a container is an instance of that image with an isolated runtime environment.

**Q3. What is Docker daemon?**

The Docker daemon is a background service that manages Docker objects and processes Docker API requests.

**Q4. What is port mapping?**

Port mapping publishes a container port on a host port, allowing external access to a service running inside the container.

**Q5. What is the difference between `docker stop` and `docker rm`?**

`docker stop` stops a running container, while `docker rm` removes a stopped container.

## 🏆 7. Assessment Result

**Score: 10/10**

Topics assessed:
- Docker architecture
- Images and containers
- VM vs container
- Layers and caching
- Docker commands
- Container lifecycle
- Port mapping
- Troubleshooting
- Real-world containerization use cases

## 🚀 8. Next Steps

- Day 16: Dockerize a Node.js Application
- Day 17: Docker Compose & Configuration

---

Learning by building. Troubleshooting by doing. Growing one container at a time. 🐳
