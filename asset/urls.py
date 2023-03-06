from django.urls import path
from asset import views

urlpatterns = [
    path('', views.AssetManageView, name='AssetManage_url'),
    
    #system settings urls path.
    path('categoryList/', views.CategoryListView, name='categoryList_url'),
    path('stationOfficeList/', views.StationOfficeListView, name='stationOfficeList_url'),
]