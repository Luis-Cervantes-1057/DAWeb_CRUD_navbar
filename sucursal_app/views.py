from django.shortcuts import render, redirect
from .models import Sucursal

# Create your views here.

def inicio_vistasSucursal (request):
    lassuc = Sucursal.objects.all()

    return render(request, "gestionarSucursal.html",{"missuc": lassuc})

def registrarSucursal(request):
    id_sucursal = request.POST["txtid"]
    id_provee = request.POST["txtprov"]
    nombre = request.POST["txtnom"]
    dire = request.POST["txtdire"]


    guardarsucursal= Sucursal.objects.create(id_provee=id_provee, nombre = nombre, dire=dire, id_sucursal=id_sucursal)

    return redirect("/")

def borrarSucursal(request, id_sucursal):
    suc = Sucursal.objects.get(id_sucursal=id_sucursal)
    suc.delete()

    return redirect("/")

def seleccionarSucursal(request, id_sucursal):
    suc = Sucursal.objects.get(id_sucursal= id_sucursal)
    
    return render (request, "editarSucursal.html", {"missuc":suc})

def editarSucursal(request):
    id_sucursal = request.POST["txtid"]
    id_provee = request.POST["txtprov"]
    nombre = request.POST["txtnom"]
    dire = request.POST["txtdire"]
    
    prov = Sucursal.objects.get(id_sucursal=id_sucursal)

    prov.id_provee = id_provee
    prov.nombre = nombre
    prov.dire = dire
    prov.save()
    return redirect("/")