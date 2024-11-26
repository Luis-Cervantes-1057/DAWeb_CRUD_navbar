from django.urls import path
from ventas_app import views

urlpatterns = [
    path("venta", views.inicio_vistasVentas, name="venta"),
    path("registrarVenta/", views.registrarVenta, name="registrarVenta"),
    
    path("borrarVenta/<id_venta>", views.borrarVenta, name="borrarVenta"),
    path("seleccionarVenta/<id_venta>", views.seleccionarVenta, name="seleccionarVenta"),
    path("editarVenta/", views.editarVenta, name="editarVenta")
]