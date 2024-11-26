from django.urls import path
from sucursal_app import views

urlpatterns = [
    path("sucursal", views.inicio_vistasSucursal, name="sucursal"),
    path("registrarSucursal/", views.registrarSucursal, name="registrarSucursal"),
    
    path("borrarSucursal/<id_sucursal>", views.borrarSucursal, name="borrarSucursal"),
    path("seleccionarSucursal/<id_sucursal>", views.seleccionarSucursal, name="seleccionarSucursal"),
    path("editarSucursal/", views.editarSucursal, name="editarSucursal")
]