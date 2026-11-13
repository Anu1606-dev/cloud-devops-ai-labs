# Day 7 — Troubleshooting Runbook

## Incident 1: Service stopped

**Symptom:** Application on port 8080 is unavailable.

**Checks:**
- `systemctl status day7-demo --no-pager`
- `sudo ss -lntp | grep ':8080'`
- `curl -I --max-time 5 http://127.0.0.1:8080`
- `journalctl -u day7-demo -n 15 --no-pager`

**Findings:** Service was inactive, no listener existed, and curl returned Connection refused.

**Root cause:** The service had been deliberately stopped.

**Fix:** `sudo systemctl start day7-demo`

**Verification:** Service active, port listening, HTTP 200.

---

## Incident 2: Network interface accessibility

**Symptom:** Localhost works, but the WSL network IP request fails.

**Checks:**
- `sudo ss -lntp | grep ':8080'`
- `ip -br addr`
- `curl -I http://127.0.0.1:8080`
- `curl -I http://172.31.137.139:8080`

**Findings:** Listener was bound to 127.0.0.1. Localhost returned 200, while the network IP returned Connection refused.

**Root cause:** The service was listening only on the loopback interface.

**Diagnostic test:** Temporarily used 0.0.0.0 and verified both addresses. Then restored 127.0.0.1.

**Final state:** Local-only listener on 127.0.0.1:8080.

**Note:** This was a bind-address issue, not proof of a firewall block. Firewall utilities were unavailable, and no firewall rule was tested or changed.

---

## Incident 3: HTTP 404 — Page not found

**Symptom:** Request to /day7-missing.html returned HTTP 404.

**Checks:**
- `curl -i http://127.0.0.1:8080/day7-missing.html`
- `ls -l ~/cloud-labs/day7-missing.html`
- `journalctl -u day7-demo -n 10 --no-pager`

**Findings:** The server was running, but the requested file did not exist initially. Logs recorded the 404.

**Root cause:** Missing HTML file.

**Fix:** Created day7-missing.html in the server's working directory.

**Verification:** The same URL returned HTTP 200 and the HTML content. Logs recorded the successful GET request.

---

## General troubleshooting sequence

1. Identify the symptom.
2. Check service status.
3. Check whether the expected port is listening.
4. Test the endpoint with curl.
5. Inspect service logs.
6. Identify the root cause before changing configuration.
7. Apply the smallest appropriate fix.
8. Verify the service, listener and HTTP response.

## Key diagnostic distinctions

| Result | Meaning |
|---|---|
| Connection refused | No accepting listener at that address/port, or an active rejection |
| Connection timed out | No response within the timeout; filtering or routing issues are possible |
| HTTP 404 | Server responded, but the requested resource was not found |
| HTTP 502 | A gateway or proxy received an invalid response from an upstream service |
| HTTP 200 | Request succeeded |

**Day 7 takeaway:** Diagnose first, change second, verify last.
