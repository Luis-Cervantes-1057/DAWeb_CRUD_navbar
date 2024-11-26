from django.db import models

class Empleado(models.Model):
    id_empleado = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=50)
    rfc = models.CharField(max_length=15)
    curp = models.CharField(max_length=18)
    num_tel = models.CharField(max_length=10)
    dire = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='fotos_empleado/', null=True, blank=True)

    def __str__(self):
        return self.nombre 
