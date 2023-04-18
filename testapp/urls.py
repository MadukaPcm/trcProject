from django.urls import path
from testapp import views

#paths for account app.
urlpatterns = [
    path('', views.TestView, name='test_url'),
]