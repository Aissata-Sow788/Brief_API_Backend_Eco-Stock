from .models import Warehouse, Product
from rest_framework import serializers
import re

# Serializer pour le modèle Warehouse
class WarehouseSerializers(serializers.ModelSerializer):

    # Configuration du serializer
    class Meta:
        # Modèle concerné
        model = Warehouse

        # Inclut tous les champs du modèle
        fields = "__all__"

    # Validation du champ "nom"
    def validate_nom(self, value):

        # Vérifie que le nom contient au moins 3 caractères
        if len(value) < 3:
            raise serializers.ValidationError(
                "Le nom doit avoir au moins 3 caractères"
            )

        # Expression régulière :
        # - uniquement des lettres
        # - un seul espace entre les mots
        # - pas d'espace au début ni à la fin
        regex = r'^[A-Za-zÀ-ÿ]+(?: [A-Za-zÀ-ÿ]+)*$'

        # Vérifie que le nom respecte le format
        if not re.fullmatch(regex, value):
            raise serializers.ValidationError(
                "Le nom ne doit contenir que des lettres, avec un seul espace entre les mots, sans espace au début ni à la fin."
            )

        # Retourne la valeur validée
        return value

    # Validation du champ "localisation"
    def validate_localisation(self, value):

        # Vérifie que la localisation contient au moins 3 caractères
        if len(value) < 3:
            raise serializers.ValidationError(
                "La localisation doit avoir au moins 3 caractères"
            )
        
        # Expression régulière :
        # - uniquement des lettres
        # - un seul espace entre les mots
        # - pas d'espace au début ni à la fin
        regex = r'^[A-Za-zÀ-ÿ]+(?: [A-Za-zÀ-ÿ]+)*$'

        # Vérifie que le nom respecte le format
        if not re.fullmatch(regex, value):
            raise serializers.ValidationError(
                "Le nom ne doit contenir que des lettres, avec un seul espace entre les mots, sans espace au début ni à la fin."
            )

        return value

    # Validation du champ "capacite"
    def validate_capacite(self, value):

        # Vérifie que la capacité est strictement positive
        if value <= 0:
            raise serializers.ValidationError(
                "La capacité doit être supérieure à 0"
            )

        # Retourne la valeur validée
        return value


# Serializer pour le modèle Product
class ProductSerializers(serializers.ModelSerializer):

    # Configuration du serializer
    class Meta:
        # Modèle concerné
        model = Product

        # Inclut tous les champs du modèle
        fields = "__all__"

    # Validation du champ "nom"
    def validate_nom(self, value):

        # Vérifie que le nom contient au moins 3 caractères
        if len(value) < 3:
            raise serializers.ValidationError(
                "Le nom doit avoir au moins 3 caractères"
            )


        # Expression régulière :
        # - uniquement des lettres
        # - un seul espace entre les mots
        # - pas d'espace au début ni à la fin
        regex = r'^[A-Za-zÀ-ÿ]+(?: [A-Za-zÀ-ÿ]+)*$'

        # Vérifie le format du nom
        if not re.fullmatch(regex, value):
            raise serializers.ValidationError(
                "Le nom ne doit contenir que des lettres, avec un seul espace entre les mots, sans espace au début ni à la fin."
            )

        return value

    # Validation du champ "quantite"
    def validate_quantite(self, value):

        # Vérifie que la quantité est strictement positive
        if value <= 0:
            raise serializers.ValidationError(
                "La quantité doit être supérieure à 0"
            )

        return value