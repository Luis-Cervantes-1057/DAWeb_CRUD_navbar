# Generated by Django 5.1.2 on 2024-11-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('id_provee', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('dire', models.CharField(max_length=100)),
            ],
        ),
    ]
