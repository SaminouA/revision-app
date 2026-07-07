terraform {
  required_version = ">= 1.6.0"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_cloud_run_v2_service" "app" {
  name     = "revision-app"
  location = var.region

  template {
    containers {
      image = var.image

      ports {
        container_port = 8080
      }
    }
  }
}
