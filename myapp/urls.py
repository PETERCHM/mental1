# yourapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forums/', views.forums, name='forums'),
    path('login/', views.login_view, name='login'),
    path('login/register/', views.register_view, name='register'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_professional/', views.create_professional, name='create_professional'),
    path('professional_profile/<int:pk>/', views.professional_profile, name='professional_profile'),
    path('create_mental_health_profile/', views.create_mental_health_profile, name='create_mental_health_profile'),
    path('mental_health_profile/<int:pk>/', views.mental_health_profile, name='mental_health_profile'),

]
