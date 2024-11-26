from django.shortcuts import render, redirect
from .models import Ventas

# Create your views here.

def inicio_vistasVentas (request):
    lasventas = Ventas.objects.all()

    return render(request, "gestionarVentas.html",{"misv": lasventas})

def registrarVenta(request):
    id_venta = request.POST["txtid"]
    id_empleado = request.POST["txtidem"]
    id_cliente = request.POST["txtidcl"]
    id_producto = request.POST["txtidprod"]
    fe_venta = request.POST["txtfecha"]
    cantidad = request.POST["txtcantidad"]


    guardarventa= Ventas.objects.create(id_cliente=id_cliente, id_venta = id_venta, id_empleado=id_empleado, id_producto=id_producto, fe_venta=fe_venta, cantidad= cantidad)

    return redirect("venta")

def borrarVenta(request, id_venta):
    venta = Ventas.objects.get(id_venta=id_venta)
    venta.delete()

    return redirect("venta")

def seleccionarVenta(request, id_venta):
    venta = Ventas.objects.get(id_venta= id_venta)
    
    return render (request, "editarVentas.html", {"misv":venta})

def editarVenta(request):
    id_venta = request.POST["txtid"]
    id_empleado = request.POST["txtidem"]
    id_cliente = request.POST["txtidcl"]
    id_producto = request.POST["txtidprod"]
    fe_venta = request.POST["txtfecha"]
    cantidad = request.POST["txtcantidad"]
    
    venta = Ventas.objects.get(id_venta=id_venta)

    venta.id_empleado = id_empleado
    venta.id_cliente = id_cliente
    venta.id_producto = id_producto
    venta.fe_venta= fe_venta
    venta.cantidad = cantidad
    venta.save()
    return redirect("venta")