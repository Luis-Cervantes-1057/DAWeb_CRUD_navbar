from django.shortcuts import render, redirect
from .models import Productos

# Create your views here.

def inicio_vistasProducto (request):
    losprod = Productos.objects.all()

    return render(request, "gestionarProductos.html",{"misproductos": losprod})

def registrarProducto(request):
    id_prod = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    sabor = request.POST["txtsabor"]
    precio = request.POST["numprecio"]
    peso = request.POST["numpeso"]
    id_proveedor = request.POST["txtidproveedor"]

    guardarproducto= Productos.objects.create(id_prod=id_prod, nombre=nombre, sabor=sabor, precio=precio, peso=peso, id_proveedor=id_proveedor)

    return redirect("/")

def borrarProducto(request, id_prod):
    prod = Productos.objects.get(id_prod=id_prod)
    prod.delete()

    return redirect("/")

def seleccionarProducto(request, id_prod):
    prod = Productos.objects.get(id_prod= id_prod)
    
    return render (request, "editarProductos.html", {"misproductos":prod})

def editarProducto(request):
    id_prod = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    sabor = request.POST["txtsabor"]
    precio = request.POST["numprecio"]
    peso = request.POST["numpeso"]
    id_proveedor = request.POST["txtidproveedor"]
    
    prod = Productos.objects.get(id_prod=id_prod)

    prod.nombre= nombre
    prod.sabor = sabor
    prod.precio = precio
    prod.peso = peso
    prod.id_proveedor = id_proveedor
    prod.save()
    return redirect("/")