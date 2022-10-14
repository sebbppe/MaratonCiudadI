from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Calle(models.Model):
    tipo=models.CharField(max_length=50)
    numero=models.CharField(max_length=50)
    orientacion=models.CharField(max_length=50)
class Carrera(models.Model):
    tipo=models.CharField(max_length=50)
    numero=models.CharField(max_length=50)
    orientacion=models.CharField(max_length=50)
class Via(models.Model):
    calle=models.ForeignKey(Calle,on_delete=models.CASCADE)
    carrera=models.ForeignKey(Carrera,on_delete=models.CASCADE)
    
class Propietario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
class Vehiculo(models.Model):
    tipo=models.CharField(max_length=50)
    capacidad=models.IntegerField(max_length=5)
    placa=models.CharField(max_length=50)
    propietatio=models.ForeignKey(Propietario,on_delete=models.CASCADE)
class semaforo(models.Model):
    tipoA=models.CharField(max_length=50)
    numA=models.IntegerField(max_length=10)
    tipoB=models.CharField(max_length=50)
    numB=models.IntegerField(max_length=10)
    estado=models.CharField(max_length=10)
    