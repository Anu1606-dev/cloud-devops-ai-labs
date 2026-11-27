# Day 30 — Lab 4: Technical Interview Preparation

## Project Introduction
I built a Cloud Support Assistant using Node.js, Express,
Python, FastEmbed, and a prepared troubleshooting knowledge base.

The application retrieves relevant documents using semantic
search and provides a mock troubleshooting response.

I also practiced Docker, application observability,
security testing, and Terraform fundamentals.

## Cloud Fundamentals
1. What is cloud computing?
   On-demand access to computing resources over a network.

2. What is EC2?
   AWS virtual compute infrastructure.

3. What is IAM?
   Identity and Access Management for controlling permissions.

4. What is a VPC?
   An isolated virtual network in AWS.

5. What is S3?
   AWS object storage.

## Linux and Networking
6. How do you investigate service failure?
   Inspect service status, logs, processes, and connectivity.

7. What is systemctl?
   A utility for managing systemd services.

8. What is journalctl?
   A utility for reading systemd journal logs.

9. How do you troubleshoot DNS?
   Use getent hosts and other DNS diagnostic tools.

10. Difference between HTTP 502 and 503?
    502 indicates an invalid upstream response.
    503 indicates a service is unavailable.

## Docker
11. What is Docker?
    A platform for building and running containers.

12. What is an image?
    A template used to create containers.

13. What is a volume?
    Persistent storage independent of container lifecycle.

14. How do you investigate a stopped container?
    Use docker ps -a, docker inspect, and docker logs.

15. What is a healthcheck?
    A configured test of container application health.

## Terraform
16. What is Terraform?
    An Infrastructure as Code tool.

17. What does terraform plan do?
    Previews proposed infrastructure changes.

18. What is Terraform state?
    A record of resources managed by Terraform.

19. What is configuration drift?
    A difference between actual infrastructure and
    the expected configuration or state.

20. Did this project provision AWS resources?
    No. The Terraform exercise used a local provider.

## AI and RAG
21. What is an embedding?
    A numerical vector representation of content.

22. What is semantic search?
    Searching based on meaning and similarity.

23. What is RAG?
    Retrieval-Augmented Generation combines retrieved context
    with a language model's generation process.

24. Does the project use a live LLM?
    No. It uses a mock response adapter. Live inference
    is not enabled.

25. What is prompt injection?
    An attempt to manipulate a model through untrusted input.

## Application Support
26. How would you troubleshoot HTTP 503?
    Inspect logs, service health, resource usage, upstream
    dependencies, and network connectivity.

27. Why use request IDs?
    To correlate logs belonging to the same request.

28. Why use metrics?
    To observe application behavior and detect failures.

29. Why use rate limiting?
    To control request frequency and protect APIs.

30. How do you validate an application?
    Use unit tests, syntax checks, healthchecks, endpoint
    tests, and input validation.

## Interview Strategy
- Explain the problem and troubleshooting sequence.
- Describe only tools actually used.
- Distinguish implemented functionality from future work.
- Do not claim live LLM inference or AWS deployment.
