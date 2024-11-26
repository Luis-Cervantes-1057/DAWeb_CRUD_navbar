from django.urls import path
from proveedor_app import views

urlpatterns = [
    path("proveedor", views.inicio_vistasProveedor, name="proveedor"),
    path("registrarProv/", views.registrarProv, name="registrarProv"),
    
    path("borrarProv/<id_provee>", views.borrarProv, name="borrarProv"),
    path("seleccionarProv/<id_provee>", views.seleccionarProv, name="seleccionarProv"),
    path("editarProv/", views.editarProv, name="editarProv")
]