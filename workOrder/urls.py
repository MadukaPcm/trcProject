from django.urls import path
from workOrder import views

urlpatterns = [
    path('', views.WorkOrderView, name='WorkOrder_url'),
]