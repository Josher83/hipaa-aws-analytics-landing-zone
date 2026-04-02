# HIPAA-Compliant AWS Analytics Landing Zone

## Project Overview
This project demonstrates the design and implementation of a **HIPAA-compliant analytics landing zone on AWS**, including automated infrastructure provisioning, secure data storage, ETL processing, and analytics visualization with Tableau.  

It is intended to align with the skills required for a **Cloud Analytics Infrastructure Engineer** role, showcasing cloud, DevOps, and analytics capabilities.

---

## Goals
- Deploy a **secure AWS environment** suitable for healthcare analytics workloads.
- Automate infrastructure using **Terraform** (IaC).
- Process and protect sensitive data with a simple **ETL pipeline**.
- Build a **Tableau dashboard** for analytics visualization.
- Demonstrate progressive complexity through **stepwise commits**, reflecting practical cloud engineering skills.

---

## Technologies
- **Cloud:** AWS (S3, EC2, VPC, CloudWatch)
- **IaC & Automation:** Terraform Cloud, GitHub Actions (CI/CD)
- **Analytics & ETL:** Python (pandas, boto3), Tableau
- **Security & Compliance:** IAM roles, S3 encryption (SSE-KMS), CloudTrail logging

---

## Setup Instructions

### Prerequisites
- Terraform Cloud account and organization
- AWS account with appropriate permissions
- GitHub repository (this one)

### Terraform Cloud Setup
1. Create two workspaces in Terraform Cloud:
   - `hipaa-aws-analytics-landing-zone-dev` (for development)
   - `hipaa-aws-analytics-landing-zone-prod` (for production)
2. Connect each workspace to this GitHub repository.
3. *This project uses Terraform Cloud dynamic credentials (OIDC) to authenticate to AWS.
4. Configure workspace-specific variables in Terraform Cloud or use the provided `.tfvars` files.

### Environment Management
- **Dev Environment**: Use `terraform.tfvars.dev` for development settings
- **Prod Environment**: Use `terraform.tfvars.prod` for production settings (includes additional subnets for HA)
- Switch between environments using Terraform workspaces: `terraform workspace select dev`

### Local Development (Optional)
If you prefer to run Terraform locally:
1. Install Terraform CLI (>= 1.0)
2. Configure AWS credentials via AWS CLI or environment variables
3. Create and select workspace: `terraform workspace select dev` or `terraform workspace new prod`
4. Copy the appropriate tfvars file: `cp terraform.tfvars.dev terraform.tfvars`
5. Comment out the `backend "remote"` block in `main.tf`
6. Run `terraform init`, `terraform plan`, `terraform apply`

---
## Project Structure
```
.
├── main.tf                          # Root Terraform configuration with module calls
├── variables.tf                     # Input variables
├── outputs.tf                       # Output values
├── terraform.tfvars.dev             # Development environment variables
├── terraform.tfvars.prod            # Production environment variables
├── modules/
│   ├── vpc/                         # VPC infrastructure module
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── s3/                          # S3 data lake module
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── .gitignore
└── README.md
```

---
## Stepwise Commit Plan

### Commit 1 – Base Landing Zone
- Modular Terraform scripts to create:
  - VPC module: VPC, subnets, security groups, NAT gateways
  - S3 module: Encrypted data lake bucket
- Initial README with architecture overview and HIPAA notes

### Commit 2 – Sample Data & ETL
- Add **dummy healthcare dataset** (CSV)
- Python ETL script to:
  - Mask sensitive information
  - Move processed data to secure S3 bucket
- Update README with ETL workflow

### Commit 3 – Tableau Dashboard
- Deploy Tableau (local or EC2)
- Connect to processed data
- Build a simple dashboard (patient counts, dummy metrics)
- Include screenshots or workbook in repository

### Commit 4 – Automation / IaC Enhancement
- Modularize Terraform scripts for reusability
- Add **GitHub Actions workflow** for validating & deploying Terraform
- Optional: CloudWatch logging for monitoring

### Commit 5 – Mini AI/ML Integration
- Train a simple ML model (e.g., patient risk score)
- Output predictions to S3
- Integrate predictions into Tableau dashboard

---

## Expected Outcomes
- Secure AWS landing zone demonstrating **HIPAA awareness**
- ETL workflow for sample healthcare data
- Tableau dashboard showing analytics insights
- Infrastructure automation and CI/CD pipeline
- Progressive, visible commits demonstrating **continuous improvement**

---
## Authentication

- This project uses Terraform Cloud dynamic credentials (OIDC) to authenticate to AWS.

- No long-lived AWS access keys are stored in this repository or in Terraform Cloud.

- How it works:

   Terraform Cloud requests a short-lived identity token
   AWS validates the token via an OIDC provider (app.terraform.io)
   Terraform Cloud assumes an IAM role in AWS
   Temporary credentials are issued for each run

- Required AWS setup:

   OIDC Identity Provider: https://app.terraform.io
   IAM Role with sts:AssumeRoleWithWebIdentity
   Appropriate permissions (AdministratorAccess for development)

- Terraform Cloud configuration:

   Workspace uses Dynamic AWS Credentials
   Role ARN is configured in workspace settings

- This approach follows modern security best practices and avoids static credentials.
---

## Notes
- Dataset is **synthetic and HIPAA-safe**.  
- Focus is on **architecture, automation, and analytics** rather than scale.  
- Project will be expanded incrementally through multiple commits.
