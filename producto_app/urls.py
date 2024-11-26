from django.urls import path
from producto_app import views

urlpatterns = [
    path("producto", views.inicio_vistasProducto, name="producto"),
    path("registrarProducto/", views.registrarProducto, name="registrarProducto"),
    
    path("borrarProducto/<id_prod>", views.borrarProducto, name="borrarProducto"),
    path("seleccionarProducto/<id_prod>", views.seleccionarProducto, name="seleccionarProducto"),
    path("editarProducto/", views.editarProducto, name="editarProducto")
]