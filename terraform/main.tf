terraform {
  required_version = ">= 1.3.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Example resource group for Smart DevOps Platform
resource "azurerm_resource_group" "devops_rg" {
  name     = var.resource_group_name
  location = var.location
}
