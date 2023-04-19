from django.urls import path
from testapp import views

#paths for account app.
urlpatterns = [
    path('', views.TestView, name='test_url'),
    path('tests/', views.TestsView, name='tests_url'),
]