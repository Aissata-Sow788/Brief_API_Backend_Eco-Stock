from django.shortcuts import render
from rest_framework import viewsets
from .models import Warehouse, Product
from .serializers import WarehouseSerializers, ProductSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework import status


# ViewSet pour gérer les entrepôts (Warehouse)
class WarehouseViewset(viewsets.ModelViewSet):
    # Récupère tous les entrepôts de la base de données
    queryset = Warehouse.objects.all()

    # Sérialiseur utilisé pour convertir les objets Warehouse en JSON
    serializer_class = WarehouseSerializers

    # Les utilisateurs non connectés peuvent uniquement lire les données.
    # Les utilisateurs authentifiés peuvent effectuer toutes les opérations (CRUD).
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Action personnalisée accessible avec :
    # GET /warehouses/<id>/audit/
    @action(detail=True, methods=['get'], url_path='audit')
    def audit(self, request, pk=None):
        # Récupère l'entrepôt correspondant à l'id fourni dans l'URL
        warehouse = self.get_object()

        # Compte le nombre de produits appartenant à cet entrepôt
        # (products est le related_name défini dans la clé étrangère)
        total_produit = warehouse.products.count()

        # Retourne un rapport (audit) de l'entrepôt
        return Response({
            "warehouse_id": warehouse.id,
            "warehouse_nom": warehouse.nom,
            "total_produits": total_produit,
        }, status=status.HTTP_200_OK)


# ViewSet pour gérer les produits (Product)
class ProductViewset(viewsets.ModelViewSet):
    # Récupère tous les produits
    queryset = Product.objects.all()

    # Sérialiseur utilisé pour convertir les objets Product en JSON
    serializer_class = ProductSerializers

    # Les utilisateurs non connectés peuvent uniquement consulter les produits
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Action personnalisée permettant de transférer un produit
    # POST /products/<id>/transfer/
    @action(detail=True, methods=['post'], url_path='transfer')
    def move(self, request, pk=None):

        # Récupère le produit à transférer
        product = self.get_object()

        # Vérifie si le produit est périmé.
        # Un produit périmé ne peut pas être déplacé.
        if product.etat == 'perime':
            return Response(
                {"error": "Un produit périmé ne peut pas changer d'entrepôt"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Récupère l'identifiant du nouvel entrepôt envoyé dans la requête
        warehouse_id = request.data.get('warehouse_id')

        # Vérifie que le champ warehouse_id a bien été fourni
        if not warehouse_id:
            return Response(
                {"error": "Le champ 'warehouse_id' est requis"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Recherche le nouvel entrepôt dans la base de données
        try:
            nouvel_entrepot = Warehouse.objects.get(pk=warehouse_id)

        # Si l'entrepôt n'existe pas, retourne une erreur
        except Warehouse.DoesNotExist:
            return Response(
                {"error": "Entrepôt introuvable"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Affecte le produit au nouvel entrepôt
        product.warehouse = nouvel_entrepot

        # Sauvegarde la modification dans la base de données
        product.save()

        # Sérialise le produit mis à jour
        serializer = self.get_serializer(product)

        # Retourne les informations du produit après le transfert
        return Response(serializer.data, status=status.HTTP_200_OK)