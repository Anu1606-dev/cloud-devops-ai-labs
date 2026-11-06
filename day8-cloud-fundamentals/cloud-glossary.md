
# ☁️ Day 8 — AWS Cloud Fundamentals Glossary

## 🌱 Cloud Fundamentals

### Cloud Computing

Cloud computing allows us to use computing resources over the internet instead of purchasing and maintaining physical infrastructure ourselves.

For example, instead of buying a physical server, an organisation can rent a virtual server from AWS and pay according to its usage and pricing arrangement.

**Real-world example:** An e-commerce company experiences heavy traffic during a festival sale. It can increase its computing capacity to handle additional requests and reduce capacity when traffic decreases. This is an example of scalability.

**Benefits of Cloud Computing:**

- **Scalability:** Increase or decrease resources when demand changes.
- **Cost flexibility:** Avoid purchasing all hardware upfront and pay according to the chosen pricing model.
- **Availability:** Design systems to remain accessible despite certain infrastructure failures.
- **Global reach:** Deploy applications closer to users in different geographical regions.
- **Managed services:** Let cloud providers manage certain infrastructure and operational tasks.

### IaaS (Infrastructure as a Service)

IaaS provides fundamental computing infrastructure through the cloud.

The provider offers resources such as:
- Virtual machines
- Storage
- Networking
- Virtualised computing infrastructure

The customer manages the operating system, runtime, applications, configurations and much of the security above the infrastructure layer.

AWS manages the underlying physical hardware, data centres and virtualisation infrastructure.

**Example:** Amazon EC2.

### PaaS (Platform as a Service)

PaaS provides a managed platform where developers can deploy applications without directly managing the underlying servers and operating systems.

**AWS example:** AWS Elastic Beanstalk.

The platform manages much of the server provisioning, deployment infrastructure and scaling configuration.

However, customers remain responsible for their application code, dependencies, credentials, data and environment configuration.

### SaaS (Software as a Service)

SaaS provides ready-to-use software delivered over the internet. Users generally access it through a browser or application.

**Examples:** Gmail, Microsoft 365 and Salesforce.

The provider manages the underlying infrastructure, operating system and application runtime. Users manage their account-level settings, access and data according to the service.

---

## ☁️ AWS Global Infrastructure

### Region

A Region is a separate geographical area where AWS operates its cloud infrastructure.

**Examples:**
- `ap-south-1` — Asia Pacific (Mumbai)
- `ap-south-2` — Asia Pacific (Hyderabad)
- `us-east-1` — US East (N. Virginia)
- `eu-west-1` — Europe (Ireland)

**Why does Region selection matter?**

1. **Latency:** Choosing a geographically closer Region can reduce network delay for users.
2. **Compliance:** Some organisations must store data in a particular country or jurisdiction.
3. **Service availability:** Not every AWS service is available in every Region.
4. **Cost:** AWS pricing can vary between Regions.

### Availability Zone (AZ)

An Availability Zone is an isolated location within an AWS Region, consisting of one or more discrete data centres with independent infrastructure.

A Region contains multiple Availability Zones.

AZs are designed to be isolated from one another while being connected through high-bandwidth, low-latency networking.

**Important:** An AZ is not necessarily one individual data centre. It can contain multiple discrete data centres.

### High Availability (HA)

High Availability means designing a system to remain accessible with minimal downtime.

For example, if an application is deployed across multiple Availability Zones, it may continue serving users if one AZ experiences a failure, provided the application, database and networking are also designed to handle that failure.

### Fault Tolerance

Fault Tolerance means designing a system to continue operating despite specified component failures, potentially without interruption.

**Remember:** High Availability aims to minimise downtime, while Fault Tolerance generally aims for stronger continuity during failures.

---

## 🔧 AWS Core Services

### 1. Compute Services

**Amazon EC2 (Elastic Compute Cloud)**
- Provides virtual servers called instances.
- Customers choose the operating system, instance type and storage.
- Supports installing Node.js, Nginx, Python and other software.
- The customer manages the guest operating system and application environment.

**Example:** Deploy a Node.js backend on an Ubuntu EC2 instance.

**AWS Lambda**
- Runs code in response to events.
- Customers do not manage the underlying servers.
- AWS manages much of the infrastructure provisioning and scaling.
- Commonly used for event-driven automation and backend tasks.

**Example:** Automatically resize an image when someone uploads it to S3.

**AWS Elastic Beanstalk**
- A managed application deployment service.
- Developers upload their application code.
- AWS provisions and manages much of the underlying infrastructure.
- Supports platforms such as Node.js and Python.

**Example:** Deploy a Node.js application using a managed platform without manually configuring every underlying server component.

### 2. Storage Services

**Amazon S3 (Simple Storage Service)**
- Provides object storage for files and other data.
- Stores data as objects inside buckets.
- Commonly used for images, videos, backups, documents and logs.

**Example:** Store profile pictures uploaded by users of a web application.

**Amazon EBS (Elastic Block Store)**
- Provides block storage volumes for EC2.
- Works like a virtual hard disk attached to an EC2 instance.
- Commonly stores operating systems and application data.

**Example:** An Ubuntu EC2 instance uses an EBS volume for its operating system and application files.

**Amazon EFS (Elastic File System)**
- Provides managed shared file storage.
- Multiple Linux-based EC2 instances can access the same file system.
- Useful when multiple servers need access to shared files.

**Example:** Two application servers access the same shared uploads directory.

**Storage comparison:**
- S3 → Object storage.
- EBS → Block storage.
- EFS → Shared file storage.

### 3. Networking Services

**Amazon VPC (Virtual Private Cloud)**
- Provides a logically isolated network for AWS resources.
- Allows customers to define IP address ranges and subnets.
- Controls how resources are organised and connected.

**Example:** Place application servers and a database inside a VPC.

**Security Groups**
- Act as virtual firewalls for supported AWS resources.
- Control inbound and outbound network traffic.
- Rules specify protocols, ports and allowed sources or destinations.
- They are stateful: response traffic for an allowed connection is automatically permitted.

**Example:** Allow SSH on port 22 only from a trusted IP address and HTTPS on port 443 as required.

**Elastic Load Balancing (ELB)**
- Distributes incoming traffic across registered targets.
- Can route requests to healthy application instances.
- Helps improve application availability and scalability.

**Example:** Distribute website traffic between EC2 instances in two Availability Zones.

**Note:** An Application Load Balancer (ALB) is one type of Elastic Load Balancer.

**Amazon Route 53**
- AWS DNS and domain registration service.
- Routes domain queries to appropriate resources.
- Supports health checks and DNS routing policies.

**Example:** Direct `example.com` to an application's load balancer.

### 4. Database Services

**Amazon RDS (Relational Database Service)**
- Provides managed relational databases.
- Supports engines such as PostgreSQL, MySQL and MariaDB.
- AWS manages many database administration tasks, depending on the configuration.

**Example:** Store customer details and orders in a managed PostgreSQL database.

**Amazon DynamoDB**
- Fully managed NoSQL database.
- Supports key-value and document data models.
- Designed for low-latency access at scale.

**Example:** Store session information or application settings in a DynamoDB table.

**Database comparison:**
- RDS → Relational database.
- DynamoDB → NoSQL database.

### 5. Identity and Access Management

**AWS IAM (Identity and Access Management)**
- Controls who can access AWS resources and what actions they can perform.
- Uses identities, roles, policies and permissions.
- Supports the principle of Least Privilege.

**Example:** Give a developer read-only access to a specific S3 bucket without granting administrator access to the entire AWS account.

### 6. Monitoring and Observability

**Amazon CloudWatch**
- AWS monitoring and observability service.
- Collects metrics, logs and events from AWS resources and applications.
- Supports alarms and dashboards.
- Helps identify performance issues and failures.

**Example:** Monitor EC2 CPU utilisation and create an alarm when it stays above a chosen threshold.

**Interview distinction:**
- IAM → Who can access what?
- CloudWatch → What is happening with my resources?

---

## 🔐 Security

### Shared Responsibility Model

The AWS Shared Responsibility Model divides security responsibilities between AWS and its customers.

- **AWS:** Security OF the cloud.
- **Customer:** Security IN the cloud.

### Security OF the Cloud — AWS Responsibility

AWS is responsible for protecting the underlying cloud infrastructure.

This includes:

- **Physical data centres:** Building security and physical access.
- **Hardware:** Physical servers, storage devices and networking equipment.
- **Foundational networking:** Infrastructure-level network protection.
- **Virtualisation:** Hypervisor and underlying virtualisation layer.
- **Infrastructure availability:** Maintaining AWS infrastructure and facilities.

**Example:** If someone attempts unauthorised physical access to servers inside an AWS data centre, protecting that facility is AWS's responsibility.

### Security IN the Cloud — Customer Responsibility

Customers are responsible for securing the resources and configurations they control.

| Responsibility | Meaning |
|---|---|
| IAM permissions | Decide who can access AWS resources. |
| Data security | Protect application and business data. |
| Encryption | Configure encryption where required. |
| Operating system | Patch and secure the guest OS on EC2. |
| Security groups | Configure allowed inbound and outbound traffic. |
| Application security | Secure code, dependencies and configurations. |

**Example:** Suppose a customer launches an Ubuntu server using Amazon EC2.

AWS manages the physical server and underlying virtualisation infrastructure. The customer is responsible for:
- Updating Ubuntu.
- Configuring SSH access.
- Managing user permissions.
- Securing the application.
- Configuring the EC2 security group.

If a customer unnecessarily leaves SSH open to everyone, it is a customer-side configuration issue.

### Least Privilege

Least Privilege is the security principle of granting a user, application or service only the minimum permissions required to perform its intended tasks — and no more than necessary.

**Example:** If a developer only needs to view files in one S3 bucket, grant read-only access to that specific bucket rather than full administrator access to the entire AWS account.

**Why is it important?**
- Reduces the risk of unauthorised access.
- Limits the impact of compromised accounts.
- Prevents unnecessary permissions.
- Improves overall cloud security.

---

## 🎯 Quick Interview Revision

| Question | Key answer |
|---|---|
| What is IaaS? | Virtualised infrastructure such as compute, storage and networking. |
| What is PaaS? | A managed platform for deploying applications. |
| What is SaaS? | Ready-to-use software delivered over the internet. |
| What is a Region? | A separate geographical area containing AWS infrastructure. |
| What is an AZ? | An isolated infrastructure location within a Region. |
| What is High Availability? | Designing systems to minimise downtime. |
| What is Fault Tolerance? | Continuing operation despite specified failures. |
| What is EC2? | AWS virtual server compute service. |
| What is S3? | AWS object storage service. |
| What is VPC? | A logically isolated AWS network. |
| What is IAM? | AWS identity and access management service. |
| What is RDS? | Managed relational database service. |
| What is CloudWatch? | AWS monitoring and observability service. |
| What is Least Privilege? | Grant only the minimum permissions required. |

## 🌻 Day 8 Completion Record

- [x] IaaS, PaaS and SaaS.
- [x] AWS Regions and Availability Zones.
- [x] High Availability and Fault Tolerance.
- [x] Shared Responsibility Model.
- [x] AWS core services.
- [x] Final knowledge assessment — **8/8**.
- [ ] Save the glossary in the local lab directory.
- [ ] Commit and push the glossary to GitHub.

**Local proof:** `~/cloud-labs/day8-cloud-fundamentals/cloud-glossary.md`

**GitHub repository:** https://github.com/Anu1606-dev/cloud-devops-ai-labs
