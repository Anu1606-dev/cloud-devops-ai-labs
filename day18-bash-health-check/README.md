
# Day 18 — Bash Health Check Automation

## Objective
Build a Bash-based application health-check script that monitors an HTTP endpoint, detects failures, uses timeouts, records timestamps, and returns meaningful exit codes.

## Labs Completed

### Lab 1 — Bash Script Foundation
- Created `health-check.sh`
- Added Bash shebang and basic script output
- Executed using `bash` and `./`
- Set executable permissions using `chmod +x`

### Lab 2 — HTTP Health Validation
- Checked an application endpoint using `curl`
- Captured HTTP status codes
- Used conditional logic to determine application health
- Returned exit code `0` for healthy and `1` for unhealthy

### Lab 3 — Timeout Protection and Logging
- Added connection timeout of 3 seconds
- Added total request timeout of 5 seconds
- Captured curl exit codes
- Added timestamped logging
- Appended results to a log file
- Excluded generated runtime logs using `.gitignore`

### Lab 4 — Failure Simulation and Recovery
- Stopped the Node.js application using Docker Compose
- Verified failure detection (`HTTP 000`, curl exit code `7`)
- Verified script exit code `1`
- Confirmed the failure was recorded in the log
- Restarted the application
- Verified HTTP `200` and script exit code `0`

## Script Features

- HTTP health monitoring
- Timestamped execution
- Connection timeout protection
- Request timeout protection
- HTTP status validation
- Curl exit-code handling
- Persistent log entries
- Automation-friendly exit codes

## Commands Used

```bash
./health-check.sh
echo $?
cat health-check-log.txt
tail -n 5 health-check-log.txt
curl -i http://localhost:8080/health
docker compose stop app
docker compose start app
docker compose ps
```

## Exit Code Behavior

| Exit Code | Meaning |
|---|---|
| 0 | Application healthy — HTTP 200 |
| 1 | Application unhealthy or request failure |

## Technologies

- Bash
- Linux
- curl
- Docker
- Docker Compose
- HTTP
- Git

## Key Learning

A running container does not necessarily mean the application is healthy. Monitoring must validate application-level behavior, handle failures, use timeouts, maintain logs, and return exit codes that other automation tools can interpret.

## Verification

Successfully tested both healthy and unhealthy application states.

- Healthy: HTTP 200, exit code 0
- Unhealthy: HTTP 000, curl exit code 7, script exit code 1

Runtime logs are generated locally and excluded from Git tracking.
