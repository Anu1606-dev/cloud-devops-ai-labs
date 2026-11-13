# Day 13 — Serverless vs EC2

## EC2 / Virtual Machine

- Requires server provisioning.
- User manages the operating system.
- User handles server maintenance and patching.
- Typically runs long-lived processes.
- Scaling requires capacity planning and configuration.
- Charged based on instance usage and related resources.

## AWS Lambda / Serverless

- AWS manages underlying execution infrastructure.
- Runs code in response to events or requests.
- Automatically scales within service limits.
- No direct OS administration.
- Standard function invocation maximum is 15 minutes.
- Charged based on requests and execution duration.

## When to choose EC2

- Long-running applications.
- Full OS control.
- Custom system-level software.
- Continuous workloads.

## When to choose Lambda

- Event-driven processing.
- Scheduled tasks.
- File processing.
- Webhooks.
- Lightweight API backends.

## Interview Answer

EC2 provides virtual machines where we manage the server and operating system.
AWS Lambda executes code in response to events while AWS manages the
underlying infrastructure and scaling.
