from django.db import models

# Create your models here.
class Sucursal (models.Model):
    id_sucursal = models.PositiveSmallIntegerField(primary_key=True)
    id_provee = models.IntegerField()
    nombre = models.CharField(max_length=50)
    dire = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre