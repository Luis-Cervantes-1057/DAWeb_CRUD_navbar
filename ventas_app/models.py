from django.db import models

# Create your models here.

class Ventas (models.Model):
    id_venta = models.PositiveSmallIntegerField(primary_key=True)
    id_empleado = models.IntegerField()
    id_cliente = models.IntegerField()
    id_producto = models.IntegerField()
    fe_venta = models.DateTimeField()
    cantidad = models.CharField(max_length=5)

    def __str__(self):
        return self.id_venta
