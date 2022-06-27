from django.db import models


# Create your models here.

class Familiar(models.Model):
    nombre=models.CharField(max_length=100)
    telefono= models.IntegerField()
    fechaNacimiento=models.DateTimeField()

class TipoFamiliar(models.Model):
    apellido= models.CharField(max_length=200)
    parentezco= models.CharField(max_length=100)

class Hijos(models.Model):
    padre= models.CharField(max_length=200)
    madre= models.CharField(max_length=200)
    cant_hermanos= models.IntegerField()
    