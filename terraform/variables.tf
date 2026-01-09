variable "resource_group_name" {
  description = "Resource group for Smart DevOps Platform"
  type        = string
  default     = "smart-devops-rg"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "East US"
}
