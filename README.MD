#  Eco-Stock API

API REST développée avec **Django REST Framework** permettant de gérer des entrepôts et leurs produits.

## Fonctionnalités

- Gestion des entrepôts (CRUD)
- Gestion des produits (CRUD)
- Transfert d'un produit vers un autre entrepôt
- Audit d'un entrepôt
- Authentification JWT avec SimpleJWT
- Protection des routes critiques

---

# 🛠 Technologies

- Python 3
- Django
- Django REST Framework
- SimpleJWT
- SQLite
- OpenAPI

---

# Installation

## Cloner le projet

```bash
git clone https://github.com/votre-compte/eco-stock-api.git
```

```bash
cd eco-stock-api
```

## Créer un environnement virtuel

Linux / Mac

```bash
python -m venv env
source env/bin/activate
```

Windows

```bash
python -m venv env
env\Scripts\activate
```
---


## Effectuer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Créer un super utilisateur

```bash
python manage.py createsuperuser
```

---

## Lancer le serveur

```bash
python manage.py runserver
```

L'API est disponible sur :

```
http://127.0.0.1:8000/
```


---

# Authentification JWT

## Obtenir un token


### POST

```
/api/token/
```


### Body

```json
{
    "username": "Aicha",
    "password": "passer123"
}
```

Réponse

```json
{
    "refresh": "...",
    "access": "..."
}
```

---

## Rafraîchir un token

### POST

```
/api/token/refresh/
```

Body

```json
{
    "refresh": "votre_refresh_token"
}
```

---

# Authentification dans Postman

Dans l'onglet **Authorization**

Type :

```
Bearer Token
```

Puis coller le **Access Token**.

Ou dans les headers :

```
Authorization: Bearer <access_token>
```

---

# Endpoints

## Warehouse

### Lister les entrepôts

| Méthode | Endpoint |
|----------|-----------|
| GET | /api/warehouses/ |

---

### Détails d'un entrepôt

| Méthode | Endpoint |
|----------|-----------|
| GET | /api/warehouses/{id}/ |

---

### Créer un entrepôt

| Méthode | Endpoint |
|----------|-----------|
| POST | /api/warehouses/ |

Authentification requise.

---

### Modifier un entrepôt

| Méthode | Endpoint |
|----------|-----------|
| PUT | /api/warehouses/{id}/ |

Authentification requise.

---

### Modification partielle

| Méthode | Endpoint |
|----------|-----------|
| PATCH | /api/warehouses/{id}/ |

Authentification requise.

---

### Supprimer

| Méthode | Endpoint |
|----------|-----------|
| DELETE | /api/warehouses/{id}/ |

Authentification requise.

---

## Audit d'un entrepôt

### GET

```
/api/warehouses/{id}/audit/
```

Réponse

```json
{
    "warehouse_id": 1,
    "warehouse_nom": "Entrepôt Dakar",
    "total_produits": 15
}
```

---

# Product

## Lister les produits

| Méthode | Endpoint |
|----------|-----------|
| GET | /api/products/ |

---

## Détails

| Méthode | Endpoint |
|----------|-----------|
| GET | /api/products/{id}/ |

---

## Ajouter

| Méthode | Endpoint |
|----------|-----------|
| POST | /api/products/ |

Authentification requise.

---

## Modifier

| Méthode | Endpoint |
|----------|-----------|
| PUT | /api/products/{id}/ |

Authentification requise.

---

## Modification partielle

| Méthode | Endpoint |
|----------|-----------|
| PATCH | /api/products/{id}/ |

Authentification requise.

---

## Supprimer

| Méthode | Endpoint |
|----------|-----------|
| DELETE | /api/products/{id}/ |

Authentification requise.

---

# Transfert d'un produit

### POST

```
/api/products/{id}/transfer/
```

Body

```json
{
    "warehouse_id": 2
}
```

Conditions métier

- Le produit doit exister.
- L'entrepôt de destination doit exister.
- Le produit ne doit pas être périmé.

Réponse

```json
{
    "id": 3,
    "nom": "Riz",
    "quantite": 100,
    "etat": "disponible",
    "warehouse": 2
}
```

---

# Modèle de données

## Warehouse

| Champ | Type |
|---------|------|
| nom | CharField |
| localisation | CharField |
| capacite | IntegerField |

---

## Product

| Champ | Type |
|---------|------|
| nom | CharField |
| quantite | IntegerField |
| date_expiration | DateTimeField |
| etat | ChoiceField |
| warehouse | ForeignKey |

Relation

```
Warehouse (1)
      |
      |-----< Product (N)
```

---

# Règles métier

## Transfert

- Vérifie que le produit existe.
- Vérifie que l'entrepôt existe.
- Vérifie que le produit n'est pas périmé.
- Met à jour l'entrepôt du produit.

---

## Audit

Retourne :

- identifiant de l'entrepôt
- nom de l'entrepôt
- nombre total de produits

---

# Codes HTTP

| Code | Description |
|-------|-------------|
| 200 | Succès |
| 201 | Création |
| 204 | Suppression |
| 400 | Données invalides |
| 401 | Authentification requise |
| 404 | Ressource introuvable |
| 500 | Erreur serveur |

---

# Sécurité

L'API utilise **JWT (SimpleJWT)**.

Les routes suivantes nécessitent une authentification :

- POST /api/warehouses/
- PUT /api/warehouses/{id}/
- PATCH /api/warehouses/{id}/
- DELETE /api/warehouses/{id}/
- POST /api/products/
- PUT /api/products/{id}/
- PATCH /api/products/{id}/
- DELETE /api/products/{id}/
- POST /api/products/{id}/transfer/

Les routes GET restent accessibles en lecture seule.

---

# Documentation OpenAPI

L'API est documentée automatiquement grâce à **drf-spectacular**, qui génère une documentation conforme au standard **OpenAPI 3**.

## Swagger UI

Interface interactive permettant d'explorer et de tester les endpoints de l'API directement depuis le navigateur.

```
http://127.0.0.1:8000/api/docs/
```

---

## ReDoc

Documentation générée au format ReDoc, idéale pour la lecture de la documentation.

```
http://127.0.0.1:8000/api/redoc/
```

---

## Schéma OpenAPI

Le schéma OpenAPI de l'API est disponible au format YAML.

```
http://127.0.0.1:8000/api/schema/
```

---

## Configuration

Le projet utilise **drf-spectacular** pour générer automatiquement la documentation OpenAPI.

Installation :

```bash
pip install drf-spectacular
```

Configuration dans `settings.py` :

```python
INSTALLED_APPS = [
    ...
    "drf_spectacular",
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Eco-Stock API",
    "DESCRIPTION": "API REST de gestion des entrepôts et des produits",
    "VERSION": "1.0.0",
}
```

Configuration des routes dans `urls.py` :

```python
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
```

# Aissata Sow

Projet réalisé dans le cadre du développement d'une API REST avec Django REST Framework.