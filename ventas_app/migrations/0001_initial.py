# Generated by Django 5.1 on 2024-11-25 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_venta', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('id_empleado', models.IntegerField()),
                ('id_cliente', models.IntegerField()),
                ('id_producto', models.IntegerField()),
                ('fe_venta', models.DateTimeField()),
                ('cantidad', models.CharField(max_length=5)),
            ],
        ),
    ]
