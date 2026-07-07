# Revision App

Revision App est une petite API Flask utilisee pour reviser toute la chaine DevOps : Git, CI, qualite,
securite, Docker, artefacts, documentation, Infrastructure as Code, Kubernetes et GitOps.

## Demarrage

```bash
pip install -r requirements-dev.txt
python src/app.py
```

En production, l'application est servie par Gunicorn dans le conteneur Docker.
