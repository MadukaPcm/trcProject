from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.InventoryView, name='Inventory_url'),
    path('createInventory/', views.CreateInventoryView, name='createInventory_url'),
    path('updateInventory/<str:pk>', views.UpdateInventoryView, name='updateInventory_url'),
    path('isAutoIMaintained/', views.IsAutoIMaintainedView, name='isAutoIMaintained_url'),
    path('inventoryStatus/', views.InventoryStatusView, name='inventoryStatus_url'),
    path('autCallf/', views.AutoCallView, name='autCallf_url'),
]