from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.

def inicio_vistasEmpleado (request):
    losempleado = Empleado.objects.all()

    return render(request, "gestionarEmpleado.html",{"misem": losempleado})

def registrarEmpleado(request):
    id_empleado = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    rfc = request.POST["txtrfc"]
    curp = request.POST["txtcurp"]
    num_tel = request.POST["numtel"]
    dire = request.POST["txtdire"]
    sexo = request.POST["txtsex"]
    foto = request.FILES["txtfoto"]

    guardarempleado= Empleado.objects.create(id_empleado=id_empleado, nombre=nombre, apellido=apellido, num_tel=num_tel, dire=dire, rfc=rfc, curp=curp,sexo=sexo, foto=foto)

    return redirect("empleado")

def borrarEmpleado(request, id_empleado):
    em = Empleado.objects.get(id_empleado=id_empleado)
    em.delete()

    return redirect("empleado")

def seleccionarEmpleado(request, id_empleado):
    em = Empleado.objects.get(id_empleado=id_empleado)
    
    return render (request, "editarEmpleado.html", {"misem":em})


def editarEmpleado(request):
    if request.method == "POST":
        id_empleado = request.POST["txtid"]
        nombre = request.POST["txtnombre"]
        apellido = request.POST["txtapellido"]
        rfc = request.POST["txtrfc"]
        curp = request.POST["txtcurp"]
        num_tel = request.POST["numtel"]
        dire = request.POST["txtdire"]
        sexo = request.POST["txtsex"]
        
        # Obtener el objeto Empleado a editar
        em = Empleado.objects.get(id_empleado=id_empleado)

        # Verifica si hay una nueva foto
        if request.FILES.get("txtfoto"):
            em.foto = request.FILES["txtfoto"]  # Asignar la nueva foto
        else:
            # Si no se sube una nueva foto, mantenemos la foto anterior
            em.foto = request.POST.get("old_foto", em.foto)  # Si old_foto no está presente, usa la foto actual

        # Asignar los otros campos
        em.nombre = nombre
        em.apellido = apellido
        em.rfc = rfc
        em.curp = curp
        em.num_tel = num_tel
        em.dire = dire
        em.sexo = sexo

        # Guardar los cambios en la base de datos
        em.save()

        # Redirigir a otra vista, por ejemplo, a la lista de empleados
        return redirect("empleado")  # Cambia "/" si quieres redirigir a otra URL
