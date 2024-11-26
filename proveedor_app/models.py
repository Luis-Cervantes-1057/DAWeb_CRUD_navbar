from django.db import models

# Create your models here.
class Proveedor (models.Model):
    id_provee = models.PositiveSmallIntegerField(primary_key=True)
    id_empleado = models.IntegerField()
    num_vehiculo = models.CharField(max_length=10)
    id_producto = models.IntegerField()
    id_sucursal = models.IntegerField()

    def __str__(self):
        return self.id_provee