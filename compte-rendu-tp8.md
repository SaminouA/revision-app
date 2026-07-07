# Compte Rendu TP8 - Revisions et ouverture au cloud
**Usine Logicielle - Master 1 DevOps**
**Sup de Vinci 2025/2026**
**Nom : Nadira**

## Contexte

Le TP8 est realise dans un depot separe nomme `revision-app`. Il consolide les briques vues dans les TP precedents : Git, CI, qualite, securite, Docker, artefacts, documentation, Infrastructure as Code, Kubernetes et GitOps.

## Question 1 - Pourquoi utiliser gunicorn en production plutot que app.run() ?

`app.run()` est le serveur de developpement integre a Flask. Il est pratique pour tester localement, mais il n'est pas concu pour gerer une charge de production, les timeouts, les workers ou les signaux systeme. Gunicorn est un serveur WSGI robuste, capable de gerer plusieurs workers et adapte a un conteneur de production.

## Question 2 - Difference entre merge --no-ff et merge fast-forward ?

Un merge fast-forward deplace simplement la branche principale vers le dernier commit de la branche si aucun commit divergent n'existe. Il ne cree pas de commit de merge. Un merge `--no-ff` cree toujours un commit de merge, meme si un fast-forward etait possible.

On prefere souvent `--no-ff` pour une branche de fonctionnalite car il conserve une trace claire du regroupement des commits de la feature dans l'historique Git.

## Question 3 - SemVer : que faut-il incrementer ?

- Correction d'un bug : PATCH, par exemple `1.0.0` vers `1.0.1`.
- Ajout d'une route sans casser l'existant : MINOR, par exemple `1.0.0` vers `1.1.0`.
- Changement du format de reponse JSON : MAJOR, par exemple `1.0.0` vers `2.0.0`, car les clients existants peuvent casser.

## Question 4 - Pourquoi formatage et lint avant les tests ?

On place le formatage et le lint avant les tests car ces controles sont rapides et detectent vite des erreurs simples. Cela evite de lancer des tests plus longs sur un code deja invalide. Ce principe s'appelle le fail fast.

## Question 5 - Que fait --cov-fail-under=80 ?

L'option `--cov-fail-under=80` fait echouer la commande pytest si la couverture de code est inferieure a 80 %. Dans la CI, ce seuil sert de quality gate : il empeche de fusionner du code insuffisamment teste.

## Question 6 - Formatter, linter, SAST et SCA

- Black est un formatter : il applique automatiquement un style de code uniforme.
- Ruff est un linter : il detecte des erreurs de style, d'import, de qualite ou de bugs probables.
- Bandit est un outil de SAST : il analyse le code source pour trouver des failles de securite potentielles.
- pip-audit est un outil de SCA : il analyse les dependances Python pour detecter des vulnerabilites connues.

## Question 7 - Secret committe puis pousse : quelles etapes ?

Il faut d'abord considerer le secret comme compromis. Les bonnes etapes sont : revoquer ou regenerer le secret chez le fournisseur, supprimer le secret du code, ajouter une protection comme `.env` et `.gitignore`, nettoyer l'historique si necessaire avec un outil adapte, forcer le push seulement apres coordination, puis ajouter une detection de secrets dans la CI pour eviter la repetition.

## Question 8 - Pourquoi build once, deploy everywhere ?

Il ne faut pas reconstruire l'image entre staging et production car on perd la garantie que le meme artefact est teste puis deploye. Si l'image est reconstruite, une dependance, une image de base ou une configuration peut changer. Construire une seule fois et deployer partout garantit la reproductibilite, la tracabilite et un rollback fiable.

## Question 9 - Pourquoi ne jamais deployer latest en production ?

Le tag `latest` est mutable : il peut pointer vers une image differente au fil du temps. En production, cela rend les deploiements non reproductibles et les rollbacks dangereux. Il vaut mieux deployer un tag immutable comme `v1.0.0` ou un SHA.

## Question 10 - Trois avantages de Documentation as Code

La Documentation as Code apporte :

- versionnement de la documentation avec le code ;
- revue de la documentation en Pull Request ;
- generation et verification automatique en CI avec `mkdocs build --strict`.

## Question 11 - Apport de Terraform par rapport a la console web

Terraform permet de decrire l'infrastructure sous forme de code versionne. Contrairement a une creation manuelle dans une console web, il offre de la reproductibilite, de la revue de changements, un historique Git, un plan avant application et une meilleure coherence entre environnements.

## Question 12 - Cloud Run ou Kubernetes ?

Cloud Run convient lorsqu'on veut deployer rapidement des conteneurs HTTP sans gerer l'infrastructure, avec autoscaling et peu d'operations. Kubernetes est preferable pour des architectures complexes, des besoins avances de reseau, de stockage, de controle fin, de jobs, de sidecars ou de portabilite multi-cloud.

## Question 13 - Qu'est-ce que le GitOps ?

Le GitOps consiste a utiliser Git comme source de verite de l'infrastructure et des deploiements. Un outil comme Argo CD ou Flux compare l'etat du cluster avec l'etat decrit dans Git et synchronise automatiquement. Son principal interet est la tracabilite : toute modification passe par un commit et peut etre revue ou rollbackee.

## Question 14 - Service de conteneurs manage : Azure Container Apps

Service choisi : Azure Container Apps.

Principe : Azure Container Apps est une plateforme serverless pour executer des applications conteneurisees sans gerer directement les serveurs, l'orchestration ou une grande partie des details d'infrastructure. Elle peut heberger des API, des microservices, des jobs et des traitements evenementiels.

Points communs avec Cloud Run :

- les deux executent des conteneurs manages sans gestion directe des serveurs ;
- les deux fournissent de l'autoscaling et conviennent bien aux API HTTP.

Differences avec Cloud Run :

- Azure Container Apps met fortement en avant KEDA pour scaler selon de nombreux declencheurs, alors que Cloud Run est centre sur le modele Cloud Run et ses integrations Google Cloud ;
- Azure Container Apps integre des fonctionnalites comme Dapr pour les microservices, alors que Cloud Run reste plus simple et oriente service/job serverless sur Google Cloud.

Sources consultees :

- Azure Container Apps overview : https://learn.microsoft.com/en-us/azure/container-apps/overview
- Cloud Run overview : https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run

## Commandes de verification

```bash
black --check src tests
ruff check src tests
bandit -r src -ll
pip-audit -r requirements.txt
pytest --cov=src --cov-fail-under=80
mkdocs build --strict
```

## Lien du projet

https://github.com/SaminouA/revision-app
