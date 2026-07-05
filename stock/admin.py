from django.contrib import admin
from .models import Warehouse, Product


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'localisation', 'capacite')
    readonly_fields = ('id',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nom', 'quantite', 'date_expiration', 'etat', 'warehouse')
    readonly_fields = ('id',)

