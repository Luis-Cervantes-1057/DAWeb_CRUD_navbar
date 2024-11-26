from django.db import models

# Create your models here.

class Productos (models.Model):
    id_prod = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    sabor = models.CharField(max_length=15)
    precio = models.FloatField()
    peso = models.FloatField()
    id_proveedor = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre