from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Profesional(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    especialidad = forms.CharField(max_length=15)
    celular = forms.CharField(max_length=10)
    email = forms.EmailField()
    
class Paciente(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    edad = forms.IntegerField()
    celular = forms.CharField(max_length=10)  
    email = forms.EmailField()
    
class Servicio(forms.Form):
    especialidad = forms.CharField(max_length=15)    
    nombre = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=40)
    precio = forms.IntegerField()
    
class Turno(forms.Form):
    fecha = forms.DateField()
    horario = forms.TimeField()
    confirmacion = forms.BooleanField()
    
class RegistroFormulario(UserCreationForm):
    first_name = forms.CharField(label="Nombre") 
    last_name = forms.CharField(label="Apellido", initial="Pepe")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Ingrese su contraseña:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Reingrese la contraseña:", widget=forms.PasswordInput)
    
    class Meta: 
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]     