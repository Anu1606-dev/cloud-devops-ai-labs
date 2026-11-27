# Day 29 — Infrastructure as Code with Terraform

## Objective

Learn Terraform fundamentals and practise managing infrastructure declaratively using the HashiCorp Local provider.

## Tools and Technologies

- Terraform v1.17.2
- HashiCorp Local provider
- HCL (HashiCorp Configuration Language)
- Ubuntu on WSL
- Git and GitHub

## Architecture

```text
main.tf
   |
   v
Terraform CLI
   |
   v
HashiCorp Local Provider
   |
   v
cloud-support-info.txt
```

Terraform configuration describes the desired state. Terraform compares it with the current state and proposes actions to reconcile differences.

## Labs Completed

1. Installed Terraform using the official HashiCorp repository.
2. Explored Terraform CLI commands.
3. Created a Terraform configuration using the Local provider.
4. Initialized the working directory using terraform init.
5. Formatted configuration using terraform fmt.
6. Validated configuration using terraform validate.
7. Previewed changes using terraform plan.
8. Created a local file resource using terraform apply.
9. Inspected resources using terraform state and terraform show.
10. Protected Terraform state and working files using .gitignore.
11. Modified configuration and observed resource replacement.
12. Simulated manual infrastructure drift.
13. Reconciled drift using terraform apply.
14. Removed the managed resource using terraform destroy.

## Setup

Navigate to the lab:

```bash
cd day29-terraform/local-infrastructure
```

Initialize:

```bash
terraform init
```

Format and validate:

```bash
terraform fmt
terraform validate
```

Preview and apply:

```bash
terraform plan
terraform apply
```

Inspect state:

```bash
terraform state list
terraform state show local_file.cloud_support_info
terraform show
```

Destroy managed resources:

```bash
terraform destroy
```

## Important Terraform Commands

| Command | Purpose |
|---|---|
| terraform init | Initializes the working directory and installs providers |
| terraform fmt | Formats Terraform configuration |
| terraform validate | Checks configuration validity |
| terraform plan | Previews proposed changes |
| terraform apply | Applies infrastructure changes |
| terraform destroy | Destroys managed resources |
| terraform state list | Lists tracked resources |
| terraform state show | Displays a resource's state |
| terraform show | Displays current state or saved plan |

## State Management and Security

Terraform state records the relationship between configuration and managed resources.

The following are excluded from Git:

- .terraform/
- *.tfstate
- *.tfstate.*
- *.tfvars
- *.tfvars.json

The provider lock file, .terraform.lock.hcl, is retained to support reproducible provider selection.

State files can contain sensitive information. Production environments should use a secured remote backend, access controls, encryption, and state locking where supported.

## Limitations

- This is a local-only learning exercise.
- No AWS or other cloud infrastructure was provisioned.
- The Local provider manages a file, not cloud compute or networking.
- No production remote backend was configured.
- No cloud charges were incurred by this exercise.

## Key Learning Outcomes

- Infrastructure as Code (IaC)
- Declarative infrastructure management
- Terraform providers and resources
- Initialization, planning, applying, and destroying
- Terraform state and provider lock files
- Configuration drift and reconciliation
- Git hygiene for infrastructure repositories

## Future Scope

Extend this foundation with AWS resources such as IAM roles, VPCs, subnets, security groups, and EC2 instances using Terraform in a controlled, cost-aware environment.
