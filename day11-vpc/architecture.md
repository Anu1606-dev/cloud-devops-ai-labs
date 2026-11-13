# Day 11 — AWS VPC Web Application Architecture

## VPC

CIDR: 10.20.0.0/16
Region: Example AWS Region

## Public subnet — AZ A

CIDR: 10.20.1.0/24

Contains:
- EC2 Ubuntu Web Server
- Nginx Reverse Proxy
- Node.js Application

Route table:
- 10.20.0.0/16 -> local
- 0.0.0.0/0 -> Internet Gateway

## Private database subnet — AZ A

CIDR: 10.20.21.0/24

Contains:
- Private database

Route table:
- 10.20.0.0/16 -> local

## Security Groups

Web Security Group:
- TCP 80: public HTTP access if required
- TCP 443: public HTTPS access
- TCP 22: trusted administrator IP only

Database Security Group:
- TCP 5432 or 3306 as required
- Source: Web/Application Security Group only

Node.js:
- Port 3000 remains private on localhost.

## Traffic Flow

Internet User
    |
    v
Internet Gateway
    |
    v
Public Subnet Route Table
    |
    v
Web Security Group
    |
    v
EC2 Ubuntu + Nginx
    |
    v
Node.js Application (127.0.0.1:3000)
    |
    v
Private Database Subnet

## Security Decisions

- Database is not publicly accessible.
- Node.js port 3000 is not publicly exposed.
- SSH is restricted to a trusted administrator IP.
- Database access is restricted to the application tier.
- No NAT Gateway is required for this isolated database design.

## Deployment Status

Conceptual architecture only.
No AWS resources have been provisioned.
