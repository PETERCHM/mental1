# yourapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forums/', views.forums, name='forums'),
    # Add more URL patterns as needed
]
