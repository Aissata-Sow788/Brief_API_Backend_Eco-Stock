from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Warehouse(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.CharField(max_length=200)
    capacite = models.PositiveIntegerField()


    def __str__(self):
        return self.nom
    
class Product(models.Model):

    ETAT_CHOICES = [
        ("disponible", "Disponible"),
        ("reserve", "Réservé"),
        ("perime", "Périmé"),
    ]

    nom = models.CharField(max_length=100)
    quantite = models.IntegerField()
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_expiration = models.DateTimeField(auto_now_add=True)
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default="disponible")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.nom