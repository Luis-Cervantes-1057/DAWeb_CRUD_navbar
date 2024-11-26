from django.shortcuts import render, redirect
from .models import Proveedor

# Create your views here.

def inicio_vistasProveedor (request):
    losprov = Proveedor.objects.all()

    return render(request, "gestionarProveedor.html",{"misprov": losprov})

def registrarProv(request):
    id_provee = request.POST["txtid"]
    id_empleado = request.POST["txtidem"]
    num_vehiculo = request.POST["txtveh"]
    id_producto = request.POST["txtidprod"]
    id_sucursal = request.POST["txtidsuc"]


    guardarprov= Proveedor.objects.create(id_provee=id_provee, num_vehiculo = num_vehiculo, id_empleado=id_empleado, id_producto=id_producto, id_sucursal=id_sucursal)

    return redirect("/")

def borrarProv(request, id_provee):
    prov = Proveedor.objects.get(id_provee=id_provee)
    prov.delete()

    return redirect("/")

def seleccionarProv(request, id_provee):
    prov = Proveedor.objects.get(id_provee= id_provee)
    
    return render (request, "editarProveedor.html", {"misprov":prov})

def editarProv(request):
    id_provee = request.POST["txtid"]
    id_empleado = request.POST["txtidem"]
    num_vehiculo = request.POST["txtveh"]
    id_producto = request.POST["txtidprod"]
    id_sucursal = request.POST["txtidsuc"]
    
    prov = Proveedor.objects.get(id_provee=id_provee)

    prov.id_empleado = id_empleado
    prov.num_vehiculo = num_vehiculo
    prov.id_producto = id_producto
    prov.id_sucursal= id_sucursal
    prov.save()
    return redirect("/")