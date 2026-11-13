# Day 12 — S3 Security Design

## Bucket Purpose

Store private company reports and application backups.

## Security Settings

- Block Public Access: All four settings enabled.
- Object Ownership: Bucket owner enforced.
- ACLs: Disabled.
- Versioning: Enabled.
- Default Encryption: SSE-S3.
- Transport: Require HTTPS/TLS.
- Access: IAM roles and restricted bucket policies.
- Public Sharing: Use pre-signed URLs when required.
- Lifecycle: Clean up incomplete multipart uploads.
- Public access: Disabled by default.

## Cost Management

- Review retained object versions.
- Choose storage classes based on access frequency.
- Review lifecycle rules.
- Monitor storage and request usage.

## Deployment Status

Design only. No actual AWS bucket or configuration was created.
