# Day 30 — Lab 3: Infrastructure and Operations

## Linux Operations
Practiced system information, processes, disk and memory usage,
service management, and journal inspection.

Commands: uname, whoami, pwd, df, free, ps, top, systemctl,
journalctl.

## Networking
Practiced:
- ip addr
- ip route
- ss -tulpn
- getent hosts
- curl

These commands inspect interfaces, routing, listening ports,
DNS resolution, and HTTP connectivity.

## Docker Operations
Practiced:
- docker ps
- docker images
- docker inspect
- docker logs
- docker stats
- docker volume ls
- docker network ls

Validated the Cloud Support Assistant container, its healthcheck,
port mapping, and persistent FastEmbed cache.

## Terraform
Used Terraform with the local provider in Day 29.

Practiced initialization, formatting, validation, planning,
applying, state inspection, and resource destruction.

The Day 29 exercise used local resources and did not provision
AWS infrastructure.

## Troubleshooting Workflow
1. Identify the affected service.
2. Check service and container status.
3. Inspect logs.
4. Verify DNS and network connectivity.
5. Check resource utilization.
6. Identify the likely failure area.
7. Apply a controlled remediation.
8. Verify recovery.

## Limitations
This is a local infrastructure learning exercise, not a
production cloud deployment.
