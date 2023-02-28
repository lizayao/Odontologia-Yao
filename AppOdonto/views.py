from django.shortcuts import render
from django.http import HttpResponse
from AppOdonto.models import *
from AppOdonto.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# INICIO

def inicio(request):
    return render(request, "AppOdonto/inicio.html")


# CRUD PROFESIONAL

def verProfesionales(request):
    profesionales = Profesional.objects.all()
    contexto = {"profesionales":profesionales}
    return render(request, "AppOdonto/Profesionales/verProfesionales.html", contexto)

def agregarProfesional(request):
    if request.method == 'POST':
        miFormulario = ProfesionalFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesional = Profesional(nombre=informacion['nombre'], apellido=informacion['apellido'], especialidad=informacion['especialidad'], celular=informacion['celular'], email=informacion['email'])
            profesional.save()
            return render(request, "AppOdonto/inicio.html")
    else:
        miFormulario = ProfesionalFormulario()
    return render(request, "AppOdonto/Profesionales/agregarProfesional.html", {"miFormulario":miFormulario})

def borrarProfesional(request, profesional_nombre):
    profesional = Profesional.objects.get(nombre=profesional_nombre)
    profesional.delete()
    profesional = Profesional.objects.all()
    contexto = {"profesional": profesional}
    return render(request, "AppOdonto/Profesionales/verProfesionales.html", contexto)

def editarProfesional(request, profesional_nombre):
    profesional = Profesional.objects.get(nombre=profesional_nombre)
    if request.method == "POST":
        miFormulario = ProfesionalFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesional.nombre = informacion['nombre']
            profesional.apellido = informacion['apellido']
            profesional.especialidad = informacion['especialidad']
            profesional.celular = informacion['celular']
            profesional.email = informacion['email']
            profesional.save()
            return render(request, "AppOdonto/inicio.html")
    else:
        miFormulario = ProfesionalFormulario(initial={'nombre':profesional.nombre, 'apellido': profesional.apellido, 'especialidad': profesional.especialidad, 'celular': profesional.celular, 'email': profesional.email})
    return render(request, "AppOdonto/Profesionales/editarProfesional.html", {"miFormulario":miFormulario, "profesional_nombre":profesional_nombre})


# CRUD SERVICIOS (vistas basadas en clases)













# CRUD PACIENTE 
    
""" class PacienteLista(ListView):
    model = Paciente 
    template_name = "AppOdonto/pacientes/paciente_list.html"
    
class PacienteDetalle(DetailView):
    model = Paciente
    template_name = "AppOdonto/pacientes/paciente_detail.html"
    
class PacienteCrear(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ["nombre", "apellido", "edad", "celular", "email"]
    success_url = "/AppOdonto/pacientes/paciente/list"
    
class PacienteModificar(LoginRequiredMixin, UpdateView):
    model = Paciente
    fields = ["nombre", "apellido", "edad", "celular", "email"]
    success_url = "/AppOdonto/pacientes/paciente/list"
    
class PacienteEliminar(LoginRequiredMixin, DeleteView):
    model = Paciente
    success_url = "/AppOdonto/pacientes/paciente/list" """


# CRUD TURNO

""" class TurnoCrear(LoginRequiredMixin, CreateView):
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
    success_url = "/AppOdonto/inicio.html"  """
    

# REGISTRO - LOGIN - LOGOUT


def registro(request):
    if request.method == "POST":
        miFormulario = RegistroFormulario(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            return render(request, "AppOdonto/inicio.html", {'mensaje':"Usuario registrado"})
    else:
        miFormulario = RegistroFormulario()
    return render(request, "AppOdonto/autenticacion/registro.html", {"formulario1":miFormulario})

def iniciar_sesion(request): 
    if request.method == "POST":
        miFormulario = AuthenticationForm(request, data = request.POST) 
        if miFormulario.is_valid():
            usuario = miFormulario.cleaned_data.get("username") 
            contra = miFormulario.cleaned_data.get("password")
            miUsuario = authenticate(username=usuario, password=contra) 
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
  
def about(request):
    return render(request, "AppOdonto/about.html")