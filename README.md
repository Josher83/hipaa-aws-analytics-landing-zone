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
- **Analytics & ETL:** Python (pandas), Docker, Tableau
- **Security & Compliance:** IAM roles, S3 encryption (SSE-KMS), CloudTrail logging

---

## Setup Instructions

### Prerequisites
- Terraform Cloud account and organization
- AWS account with appropriate permissions
- GitHub repository (this one)

### Terraform Cloud Setup
1. Create a single workspace in Terraform Cloud:
   - `hipaa-aws-analytics-landing-zone`
2. Connect the workspace to this GitHub repository.
3. This project uses Terraform Cloud dynamic credentials (OIDC) to authenticate to AWS.

### How It Works
- Push changes to the `main` branch on GitHub
- Terraform Cloud automatically triggers a plan
- Review and apply the plan in Terraform Cloud UI
- All infrastructure runs in the cloud; no local Terraform commands needed

---
## Project Structure
```
.
├── main.tf                          # Root Terraform configuration with module calls
├── variables.tf                     # Input variables (with defaults)
├── outputs.tf                       # Output values
├── modules/
│   ├── vpc/                         # VPC infrastructure module
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── s3/                          # S3 data lake module
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── data/                            # Sample healthcare dataset
│   ├── raw/                         # Source data ingested by ETL
│   │   └── patients.csv
│   └── clean/                       # Tableau-ready ETL outputs
├── etl/
│   ├── transform.py                 # ETL transform script
│   └── requirements.txt
├── Dockerfile
├── .github/workflows/etl.yml        # GitHub Actions ETL runner (Dockerized)
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
- Deploy Tableau (Tableau Cloud or Tableau Server on EC2)
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

## Dataset Loading
- Terraform uploads files from `data/raw/` and `data/clean/` into the provisioned data lake bucket during `apply`.
- Files in `data/raw/` are written under the `raw/` prefix.
- Files in `data/clean/` are written under the `clean/` prefix.
- Changes to dataset files are detected through object ETags and will be synced on the next Terraform apply.

---
## ETL Pipeline (Docker, Non-Local)

The ETL job reads source data from `data/raw/patients.csv` and creates Tableau-ready outputs in `data/clean/`.
All transforms run in GitHub Actions using Docker, not on developer machines.

Outputs:
- `patients_clean.csv`
- `diagnosis_summary.csv`

### How ETL Runs

1. Push updates to `data/raw/patients.csv` (or ETL code changes).
2. GitHub Actions workflow `.github/workflows/etl.yml` builds the Docker image.
3. The workflow runs ETL in a container and writes outputs to `data/clean/`.
4. If outputs changed, the workflow commits and pushes updated clean files.

### Manual Trigger

Use GitHub Actions `ETL Pipeline` workflow and click **Run workflow**.

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
