# Cloud Lab Plan

## 1. Purpose
The purpose of this cloud lab is to provide a safe, low-cost sandbox environment for learning, testing, and experimentation using a cloud provider’s free tier or sandbox offering.

## 2. Scope
- Environment type: Lab / Sandbox
- Intended users: Engineers / Students / Team Members
- Duration: Temporary (tear down after use)

## 3. Cloud Provider
- Provider: (AWS / Azure / GCP / OCI)
- Account / Subscription / Compartment Name: 
- Region(s):

## 4. Lab Objectives
- Validate cloud architecture concepts
- Test application deployments
- Practice infrastructure provisioning and teardown
- Learn cost management and billing controls

## 5. Architecture Overview
**Services Used:**
- Compute: (e.g., VM size – free tier eligible)
- Networking: (VPC/VNet, subnets)
- Storage: (block/object storage – free tier)
- Security: (IAM roles, security groups)
- Optional: Load balancer, database (free tier only)

**Architecture Diagram:**
- (Link or embedded image)

## 6. Access & Security
- IAM roles/users created:
- Authentication method:
- Principle of least privilege applied: Yes / No
- MFA enabled: Yes / No

## 7. Naming & Tagging Standards
**Naming Convention:**
- lab-<service>-<env>

**Tags:**
- Environment: Lab
- Owner:
- CostCenter:

## 8. Cost Considerations
- Free-tier services only: Yes / No
- Estimated monthly cost: $0 – $X
- Paid services explicitly avoided/listed

## 9. Assumptions & Constraints
- Free-tier limits apply
- Lab resources may be auto-stopped
- No production workloads allowed

## 10. Teardown Strategy (Summary)
- Manual / Automated (Terraform / Scripts)
- Expected teardown time:
- Reference: cost_control_checklist.md

## 11. Approval
- Prepared by:
- Date:
- Approved by:

