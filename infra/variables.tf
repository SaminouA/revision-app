variable "project_id" {
  description = "GCP project id used for the Cloud Run service."
  type        = string
}

variable "region" {
  description = "GCP region where the service is described."
  type        = string
  default     = "europe-west1"
}

variable "image" {
  description = "Container image deployed to Cloud Run."
  type        = string
  default     = "ghcr.io/saminoua/revision-app:v1.0.0"
}
