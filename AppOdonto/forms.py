from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppOdonto.models import Avatar

class ProfesionalFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    especialidad = forms.CharField()
    celular = forms.CharField()
    email = forms.EmailField()
    
class ServicioFormulario(forms.Form):
    servicio = forms.CharField()
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


class RegistroFormulario(UserCreationForm):
    first_name = forms.CharField(label="Nombre") 
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Usuario")
    password1 = forms.CharField(label="Contraseña:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Reingresá la contraseña:", widget=forms.PasswordInput)
    class Meta: 
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]    
        #help_texts = {k:"" for k in fields} 
        
class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label="Modificar nombre") 
    last_name = forms.CharField(label="Modificar apellido")    
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Modificar contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}
        

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]