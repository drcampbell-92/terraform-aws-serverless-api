variable "region" {
  type    = string
  default = "us-east-1"
}

variable "project_name" {
  type    = string
  default = "tf-serverless-api"
}

variable "github_repo" {
  type        = string
  description = "GitHub repository allowed to assume the pipeline role"
  default     = "drcampbell-92/terraform-aws-serverless-api"
}