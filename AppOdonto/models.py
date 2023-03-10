from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profesional(models.Model):
    def __str__(self):
        return f"Doctor/a: {self.nombre} {self.apellido} - Especialidad: {self.especialidad}"
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    especialidad = models.CharField(max_length=25)
    celular = models.CharField(max_length=10)
    email = models.EmailField()
    
class Servicio(models.Model):
    def __str__(self):
        return f"Servicio: {self.servicio} - Especialidad: {self.especialidad} - Precio: ${self.precio}"
    servicio = models.CharField(max_length=25)
    especialidad = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=80)
    precio = models.IntegerField()
    
class Paciente(models.Model):
    def __str__(self):
        return f"Paciente: {self.nombre} {self.apellido} - Celular: {self.celular} - Email: {self.email}"
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    edad = models.IntegerField()
    celular = models.CharField(max_length=10)  
    email = models.EmailField()

class Turno(models.Model):
    def __str__(self):
        return f"Paciente: {self.paciente} - Servicio: {self.servicio} - Fecha: {self.fecha} - Horario: {self.horario}"
    paciente = models.CharField(max_length=40) 
    servicio = models.CharField(max_length=25) 
    profesional = models.CharField(max_length=25)
    fecha = models.CharField(max_length=10)
    horario = models.CharField(max_length=10)
        
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    def __str__(self):
        return f"{self.usuario} - {self.imagen}"