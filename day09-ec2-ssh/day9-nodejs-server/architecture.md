# Day 9 — EC2 Node.js Application Architecture

## Request Flow

Internet User
     |
     v
Internet Gateway (attached to VPC)
     |
     v
VPC Public Subnet
(Route Table: 0.0.0.0/0 -> Internet Gateway)
     |
     v
EC2 Security Group
(Inbound TCP 80/443)
     |
     v
EC2 Ubuntu Instance
     |
     v
Nginx Reverse Proxy (80/443)
     |
     v
Node.js Application (127.0.0.1:3000)

## Administration

Administrator
     |
     | SSH (TCP 22, trusted IP only)
     v
EC2 Ubuntu Instance

## Components

- VPC: Isolated AWS virtual network.
- Internet Gateway: Enables internet connectivity for the VPC.
- Public Subnet: Subnet with a route to the Internet Gateway.
- Route Table: Routes internet-bound IPv4 traffic through the gateway.
- EC2: Hosts the application.
- Security Group: Controls permitted network traffic.
- Nginx: Reverse proxy handling public HTTP/HTTPS requests.
- Node.js: Runs the backend application on localhost port 3000.

## Security

- SSH (22): Restrict to trusted administrator IPs.
- HTTP (80): Allow only if public HTTP access or HTTPS redirection is required.
- HTTPS (443): Allow public access when HTTPS is configured.
- Node.js (3000): Keep private; do not expose it publicly.
- Use SSH key authentication.
- Keep secrets outside source control.
