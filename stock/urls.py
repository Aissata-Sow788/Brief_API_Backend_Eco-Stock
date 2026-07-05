from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WarehouseViewset, ProductViewset


# Création d'un routeur DRF.
# Le routeur génère automatiquement les URLs des ViewSets.
router = DefaultRouter()

# Enregistrement du ViewSet des entrepôts.
# Cela crée automatiquement les routes CRUD
router.register(r'warehouses', WarehouseViewset)

# Enregistrement du ViewSet des produits.
# Le routeur crée automatiquement les routes CRUD 
router.register(r'products', ProductViewset)

# Génère toutes les URLs enregistrées par le routeur
# et les rend accessibles dans l'application.
urlpatterns = router.urls

