
# Day 25 — Lab 5: RAG-Assisted Incident Troubleshooting

## Incident
A cloud-hosted Linux VM runs a Node.js API.
Users intermittently receive HTTP 503 Service Unavailable.
The service worked earlier. The root cause is unknown.

## 1. Confirm Service Health
- Check Node.js and reverse proxy service status.
- Inspect running processes and listening ports.
- Record service uptime and restart history.

Commands:
- systemctl status <service>
- pgrep -af 'node|pm2|nginx'
- ss -tulpn

## 2. Inspect Logs
- Review systemd journal.
- Inspect application logs.
- Inspect Nginx error logs if applicable.
- Look for timeouts, crashes and upstream connection errors.

Commands:
- journalctl -u <service> -n 100 --no-pager
- tail -n 100 /var/log/nginx/error.log

## 3. Investigate Network
- Verify DNS resolution.
- Test local application HTTP responsiveness.
- Check upstream dependency connectivity.

Commands:
- getent hosts <hostname>
- curl -i --max-time 5 http://127.0.0.1:<port>/health

## 4. Inspect Resources
- Check available memory and CPU load.
- Check filesystem and inode capacity.
- Investigate possible OOM events.

Commands:
- free -h
- uptime
- df -h
- df -i
- dmesg -T | grep -iE 'oom|killed process'

## 5. RAG Evidence
Retrieved documents:
- Network troubleshooting
- Service troubleshooting
- Memory troubleshooting
- Disk troubleshooting

These documents provide diagnostic guidance, not proof of the root cause.

## 6. Operational Decision
- Preserve logs and metrics.
- Perform read-only checks first.
- Separate confirmed facts from hypotheses.
- Do not restart services until sufficient diagnostic evidence is captured.

## Conclusion
The root cause remains unknown until production diagnostics are collected and evaluated.
