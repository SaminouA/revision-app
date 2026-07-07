# Revision App

![CI](https://github.com/SaminouA/revision-app/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> API Flask de revision pour consolider une chaine DevOps complete et decouvrir le deploiement cloud.

## Installation

```bash
git clone https://github.com/SaminouA/revision-app.git
cd revision-app
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements-dev.txt
python src/app.py
```

## Routes

| Route | Methode | Description |
|-------|---------|-------------|
| `/` | GET | Accueil et version |
| `/health` | GET | Health check |
| `/version` | GET | Version de l'application |

## Qualite

```bash
black --check src tests
ruff check src tests
bandit -r src -ll
pip-audit -r requirements.txt
pytest --cov=src --cov-fail-under=80
mkdocs build --strict
```

## Docker

```bash
docker build -t revision-app:v1.0.0 .
docker run -p 8080:8080 revision-app:v1.0.0
```

## Cloud

- `infra/` : exemple Terraform Cloud Run
- `k8s/` : Deployment et Service Kubernetes
- `docs/` : site MkDocs

## Licence

MIT
