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
- **IaC & Automation:** Terraform, GitHub Actions (CI/CD)
- **Analytics & ETL:** Python (pandas, boto3), Tableau
- **Security & Compliance:** IAM roles, S3 encryption (SSE-KMS), CloudTrail logging

---

## Stepwise Commit Plan

### Commit 1 – Base Landing Zone
- Terraform scripts to create:
  - VPC, subnets, security groups
  - Encrypted S3 bucket for storing sample data
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

## Notes
- Dataset is **synthetic and HIPAA-safe**.  
- Focus is on **architecture, automation, and analytics** rather than scale.  
- Project will be expanded incrementally through multiple commits.
