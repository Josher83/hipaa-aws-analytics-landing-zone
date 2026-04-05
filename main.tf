# HIPAA-Compliant AWS Analytics Landing Zone
# Terraform configuration for base infrastructure

terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }

  # Backend configuration for Terraform Cloud
  backend "remote" {
    organization = "Josher_AWS"
    workspaces {
      name = "hipaa-aws-analytics-landing-zone"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Random suffix for bucket name to ensure uniqueness
resource "random_id" "bucket_suffix" {
  byte_length = 4
}

locals {
  data_lake_bucket_name = "${var.data_lake_bucket_prefix}-${random_id.bucket_suffix.hex}"
  dataset_files         = fileset("${path.module}/data", "**")
}

# VPC Module
module "vpc" {
  source = "./modules/vpc"

  vpc_cidr             = var.vpc_cidr
  public_subnet_cidrs  = var.public_subnet_cidrs
  private_subnet_cidrs = var.private_subnet_cidrs
  enable_nat           = false # Temporarily disabled to avoid costs
}

# S3 Module
module "s3" {
  source = "./modules/s3"

  bucket_name = local.data_lake_bucket_name
}

resource "aws_s3_object" "dataset" {
  for_each = { for file in local.dataset_files : file => file }

  bucket       = module.s3.bucket_name
  key          = "raw/${each.key}"
  source       = "${path.module}/data/${each.value}"
  etag         = filemd5("${path.module}/data/${each.value}")
  content_type = each.value == "patients.csv" ? "text/csv" : null
}