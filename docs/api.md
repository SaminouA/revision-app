# API

| Route | Methode | Description |
|-------|---------|-------------|
| `/` | GET | Message d'accueil et version |
| `/health` | GET | Health check pour CI/CD, Docker et Kubernetes |
| `/version` | GET | Version applicative |

## Exemples

```bash
curl http://localhost:8080/
curl http://localhost:8080/health
curl http://localhost:8080/version
```
