# Cloud

Le TP8 prepare l'application pour plusieurs cibles cloud sans deployer reellement les ressources.

## Cloud Run

Le dossier `infra/` contient une description Terraform d'un service Cloud Run exposant le conteneur sur le port 8080.

## Kubernetes

Le dossier `k8s/` contient un Deployment avec deux replicas et un Service interne. La readiness probe appelle `/health`.

## GitOps

Les manifests Kubernetes sont versionnes dans Git. Un outil GitOps comme Argo CD ou Flux pourrait synchroniser l'etat du cluster a partir du depot.
