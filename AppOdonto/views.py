from django.shortcuts import render
from django.http import HttpResponse
from AppOdonto.models import *
from AppOdonto.forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, "AppOdonto/inicio.html")


def registro(request):
    if request.method == "POST":
        miFormulario = RegistroFormulario(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            return render(request, "AppOdonto/inicio.html")
    else:
        miFormulario = RegistroFormulario()
    return render(request, "AppOdonto/autenticacion/registro.html", {"formulario1":miFormulario})


def iniciar_sesion(request): 
    if request.method == "POST":
        miFormulario = AuthenticationForm(request, data = request.POST) 
        if miFormulario.is_valid():
            usuario = miFormulario.cleaned_data.get("username") 
            contra = miFormulario.cleaned_data.get("password")
            print(usuario)
            print(contra)
            miUsuario = authenticate(username=usuario, password=contra) 
            print(miUsuario)
            if miUsuario:
                login(request,miUsuario)          
                mensaje = f"Bienvenido {miUsuario}"
                return render(request, "AppOdonto/inicio.html", {"mensaje":mensaje})
            else:
                mensaje = f"Datos ingresados incorrectos."
                return render(request, "AppOdonto/inicio.html", {"mensaje":mensaje})
    else:
        miFormulario = AuthenticationForm()
    return render(request, "AppOdonto/autenticacion/login.html", {"formulario1":miFormulario})   


def contacto(request):
    return render(request, "AppOdonto/contacto.html")


# CRUD PROFESIONAL (solo staff)

class ProfesionalCrear(LoginRequiredMixin, CreateView):
    model = Profesional
    fields = ["nombre", "apellido", "especialidad", "celular", "email"]
    success_url = "/AppOdonto/inicio.html"
    
class ProfesionalVer(LoginRequiredMixin, ListView):
    model = Profesional 
    
class ProfesionalModificar(LoginRequiredMixin, UpdateView):
    model = Profesional
    fields = ["nombre", "apellido", "especialidad", "celular", "email"]
    success_url = "/AppOdonto/inicio.html"
    
class ProfesionalEliminar(LoginRequiredMixin, DeleteView):
    model = Profesional
    success_url = "/AppOdonto/inicio.html"


# CRUD PACIENTE

class PacienteCrear(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ["nombre", "apellido", "edad", "celular", "email"]
    success_url = "/AppOdonto/inicio.html"
    
class PacienteVer(ListView):
    model = Paciente 
    
class PacienteModificar(LoginRequiredMixin, UpdateView):
    model = Paciente
    fields = ["nombre", "apellido", "edad", "celular", "email"]
    success_url = "/AppOdonto/inicio.html"
    
class PacienteEliminar(LoginRequiredMixin, DeleteView):
    model = Paciente
    success_url = "/AppOdonto/inicio.html"


# CRUD TURNO

class TurnoCrear(LoginRequiredMixin, CreateView):
    model = Turno
    fields = ["servicio", "profesional", "fecha", "horario"]
    success_url = "/AppOdonto/inicio.html"   

class TurnoVer(LoginRequiredMixin, ListView):
    model = Turno

class TurnoModificar(LoginRequiredMixin, UpdateView):
    model = Turno
    fields = ["servicio", "profesional", "fecha", "horario"]
    success_url = "/AppOdonto/inicio.html"    

class TurnoEliminar(LoginRequiredMixin, DeleteView):
    model = Turno
    success_url = "/AppOdonto/inicio.html"
    


