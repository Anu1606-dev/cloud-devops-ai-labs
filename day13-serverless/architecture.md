# Day 13 — AWS Serverless Application Architecture

## Request Flow

Web / Mobile Client
        |
        | HTTPS Request
        v
Amazon API Gateway
        |
        | Lambda Integration
        v
AWS Lambda Function
        |
        | Executes Handler
        v
Application Logic
        |
        +------> Amazon S3
        |
        +------> Amazon DynamoDB

## Permissions

Lambda Execution Role:
- CloudWatch Logs permissions.
- Only required S3 or DynamoDB permissions.

Lambda Resource-Based Policy:
- Allows the authorised API Gateway service
  to invoke the function.

## Responsibilities

API Gateway:
- Receives HTTP requests.
- Routes requests.
- Handles configured authorisation.
- Returns API responses.

Lambda:
- Executes application code.
- Processes incoming events.
- Accesses authorised AWS services.
- Returns the function result.

CloudWatch:
- Stores application logs.
- Provides monitoring metrics.

## Security

- Apply least-privilege IAM permissions.
- Restrict who can invoke Lambda.
- Validate incoming request data.
- Use Secrets Manager for sensitive credentials.
- Configure API authorisation and throttling.
- Avoid exposing secrets in source code.

## Deployment Status

Conceptual architecture only.
No AWS resources have been created.
