from django.urls import path
from empleados_app import views

urlpatterns = [
    path("empleado", views.inicio_vistasEmpleado, name="empleado"),
    path("registrarEmpleado/", views.registrarEmpleado, name="registrarEmpleado"),
    
    path("borrarEmpleado/<id_empleado>", views.borrarEmpleado, name="borrarEmpleado"),
    path("seleccionarEmpleado/<id_empleado>", views.seleccionarEmpleado, name="seleccionarEmpleado"),
    path("editarEmpleado/", views.editarEmpleado, name="editarEmpleado")
]