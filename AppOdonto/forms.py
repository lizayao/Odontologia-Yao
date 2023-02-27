from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

""" class Profesional(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    especialidad = forms.CharField()
    celular = forms.CharField()
    email = forms.EmailField() """
    
class PacienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    celular = forms.CharField()  
    email = forms.EmailField()
    
""" class Servicio(forms.Form):
    especialidad = forms.CharField()    
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.IntegerField() """
    
class TurnoFormulario(forms.Form):
    paciente = forms.CharField()
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