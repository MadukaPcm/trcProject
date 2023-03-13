from django.urls import path
from maintenanceReport import views

urlpatterns = [
    path('', views.MaintenanceSView, name='InventoryS_url'),
]