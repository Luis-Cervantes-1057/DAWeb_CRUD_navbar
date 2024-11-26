from django.urls import path
from app_base import views

urlpatterns = [
    # Inicio CocaCola
    path('', views.inicio),
]
