from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.InventoryView, name='Inventory_url'),
]