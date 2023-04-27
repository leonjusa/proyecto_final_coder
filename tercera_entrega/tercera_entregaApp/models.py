from django.db import models
from django.contrib.auth.models import User


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'

class Tipo_cafe(models.Model):
    nombre = models.CharField(max_length=50)
    tostado = models.CharField(max_length=50)
    grano = models.CharField(max_length=50)
    cantidad_kg = models.IntegerField()
    imagen = models.ImageField(upload_to='tipo_cafe/', blank=True, null=True)

    def __str__(self):
        return f'{self.nombre}'


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.nombre}'
    
class Avatar(models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

