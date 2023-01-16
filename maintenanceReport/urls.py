from django.urls import path
from maintenanceReport import views

urlpatterns = [
    path('', views.MaintenanceSView, name='Inventory_url'),
]