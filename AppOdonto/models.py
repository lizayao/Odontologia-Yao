from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profesional(models.Model):
    def __str__(self):
        return f"Doctor/a: {self.nombre} {self.apellido} - Especialidad: {self.especialidad}"
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=15)
    celular = models.CharField(max_length=10)
    email = models.EmailField()
    
class Servicio(models.Model):
    def __str__(self):
        return f"Servicio: {self.nombre} - Especialidad: {self.especialidad} - Precio: ${self.precio}"
    nombre = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=40)
    precio = models.IntegerField()
    
class Paciente(models.Model):
    def __str__(self):
        return f"Paciente: {self.nombre} {self.apellido} - Celular: {self.celular} - Email: {self.email}"
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    edad = models.IntegerField()
    celular = models.CharField(max_length=10)  
    email = models.EmailField()
    
class Turno(models.Model):
    def __str__(self):
        return f"Paciente: {self.paciente} - Servicio: {self.servicio} - Fecha: {self.fecha} - Horario: {self.horario}"
    paciente = models.CharField(max_length=15) 
    servicio = models.CharField(max_length=15) 
    profesional = models.CharField(max_length=15)
    fecha = models.DateField()
    horario = models.TimeField()
    
class AvatarImagen(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)