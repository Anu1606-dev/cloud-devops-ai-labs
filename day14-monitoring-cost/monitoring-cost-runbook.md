# Day 14 — Cloud Monitoring & Cost Runbook

## Monitoring Objectives

- Monitor application logs.
- Monitor CPU, memory and disk usage.
- Track application errors and response latency.
- Create alarms for abnormal behaviour.
- Review CloudWatch dashboards.

## CloudWatch Logs

- Use meaningful log groups and streams.
- Search ERROR and WARN events.
- Choose an appropriate log retention period.
- Avoid logging passwords and secrets.

## Metrics and Alarms

- Monitor CPUUtilization.
- Monitor application error count.
- Monitor response latency.
- Configure meaningful thresholds.
- Review OK, ALARM and INSUFFICIENT_DATA states.
- Configure notifications where required.

## AWS Cost Management

- Review AWS Billing dashboard.
- Analyse spending through Cost Explorer.
- Set AWS Budgets alerts.
- Review Cost Anomaly Detection.
- Estimate new workloads using Pricing Calculator.
- Inspect idle EC2 and unused EBS resources.
- Review S3 object versions and lifecycle rules.
- Review CloudWatch logs and metric usage.

## Troubleshooting

- Check application logs first.
- Compare metrics across the affected period.
- Identify when the issue began.
- Check recent infrastructure or configuration changes.
- Verify whether an alarm threshold was breached.
- Record the root cause and corrective action.

## Safety

- Never assume Free Tier means zero cost.
- Review service pricing before provisioning.
- Set log retention instead of keeping all logs indefinitely.
- Avoid creating unnecessary custom metrics and dashboards.
- No AWS resources were provisioned for this exercise.
