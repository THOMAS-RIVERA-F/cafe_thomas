from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    precio = models.FloatField()
    #finca = models.ManyToOneRel()
    #imagen = models.ImageField()


class Finca(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)