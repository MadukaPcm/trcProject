from django.urls import path
from asset import views

urlpatterns = [
    path('', views.AssetView, name='Asset_url'),
]