from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfesionalFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    especialidad = forms.CharField()
    celular = forms.CharField()
    email = forms.EmailField()
    
class ServicioFormulario(forms.Form):
    nombre = forms.CharField()
    especialidad = forms.CharField()    
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    
class PacienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    celular = forms.CharField()  
    email = forms.EmailField()
    
class TurnoFormulario(forms.Form):
    paciente = forms.CharField()
    servicio = forms.CharField()
    profesional = forms.CharField()
    fecha = forms.DateField()
    horario = forms.TimeField()
    confirmacion = forms.BooleanField()



class RegistroFormulario(UserCreationForm):
    first_name = forms.CharField(label="Nombre") 
    last_name = forms.CharField(label="Apellido")
    password1 = forms.CharField(label="Ingrese su contraseña:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Reingrese la contraseña:", widget=forms.PasswordInput)
    class Meta: 
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]    
        help_texts = {k:"" for k in fields} #saca mensajes de ayuda