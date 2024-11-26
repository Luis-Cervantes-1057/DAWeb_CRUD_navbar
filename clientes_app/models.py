from django.db import models

# Create your models here.

class Clientes (models.Model):
    id_cliente = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=50)
    num_tel = models.CharField(max_length=12)
    dire = models.CharField(max_length=100)
    correo = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre