from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profesional(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=15)
    celular = models.CharField(max_length=10)
    email = models.EmailField()
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    edad = models.IntegerField()
    celular = models.CharField(max_length=10)  
    email = models.EmailField()
    
class Servicio(models.Model):
    especialidad = models.CharField(max_length=15)    
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)
    precio = models.IntegerField()
    
class Turno(models.Model):
    fecha = models.DateField()
    horario = models.TimeField()
    confirmacion = models.BooleanField()
    
class AvatarImagen(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)