# Cost Control & Teardown Checklist

## 1. Billing & Budget Configuration
- Billing enabled and verified
- Budget created: Yes / No
- Monthly budget limit: $____

## 2. Billing Alerts
| Threshold | Alert Method | Recipient |
|----------|-------------|-----------|
| 50%      | Email / SNS |           |
| 80%      | Email / SNS |           |
| 100%     | Email / SNS |           |

## 3. Cost Monitoring
- Cost Explorer / Cost Management enabled
- Daily spend reviewed: Yes / No
- Tags applied to all resources: Yes / No

## 4. Preventive Cost Controls
- Service quotas/limits configured
- Auto-shutdown enabled for compute
- Idle resources monitoring enabled
- Paid services disabled or restricted

## 5. Resource Inventory
- Compute instances
- Storage volumes / buckets
- Load balancers
- IP addresses
- Databases
- IAM roles/users
- Networking components

## 6. Teardown Procedure
**Recommended Order:**
1. Stop and delete applications
2. Terminate compute instances
3. Delete load balancers
4. Remove storage volumes and snapshots
5. Release public IPs
6. Delete networking (subnets, VPC/VNet)
7. Remove IAM roles and policies
8. Delete project/subscription (if applicable)

## 7. Automation
- IaC used (Terraform / ARM / CloudFormation): Yes / No
- Teardown command/script:
  - Example: `terraform destroy`

## 8. Post-Teardown Validation
- No active resources listed
- Billing dashboard shows $0 usage
- No orphaned resources found
- Alerts disabled or deleted

## 9. Risks & Mitigations
- Risk: Missed resource causing charges
- Mitigation: Run final billing and resource audit

## 10. Sign-off
- Teardown completed by:
- Date:
- Verified by:

