from django.shortcuts import render
#from django.http import HttpResponse
from AppOdonto.models import *
from AppOdonto.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
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

@login_required
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

@login_required
def borrarProfesional(request, profesional_nombre):
    profesional = Profesional.objects.get(nombre=profesional_nombre)
    profesional.delete()
    profesional = Profesional.objects.all()
    contexto = {"profesional": profesional}
    return render(request, "AppOdonto/Profesionales/verProfesionales.html", contexto)

@login_required
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

class ServicioList(LoginRequiredMixin, ListView):
    model = Servicio

class ServicioDetail(LoginRequiredMixin, DetailView):
    model = Servicio

class ServicioCreate(LoginRequiredMixin, CreateView):
    model = Servicio
    success_url = "/AppOdonto/servicio/list"
    fields = ['nombre', 'especialidad', 'descripcion', 'precio']
    
class ServicioUpdate(LoginRequiredMixin, UpdateView):
    model = Servicio
    success_url = "/AppOdonto/servicio/list"
    fields = ['nombre', 'especialidad', 'descripcion', 'precio']

class ServicioDelete(LoginRequiredMixin, DeleteView):
    model = Servicio
    success_url = "/AppOdonto/servicio/list"


# CRUD PACIENTE 
    
class PacienteList(LoginRequiredMixin, ListView):
    model = Paciente 
    
class PacienteDetail(LoginRequiredMixin, DetailView):
    model = Paciente
    
class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ["nombre", "apellido", "edad", "celular", "email"]
    success_url = "/AppOdonto/paciente/list"
    
class PacienteUpdate(LoginRequiredMixin, UpdateView):
    model = Paciente
    fields = ["nombre", "apellido", "edad", "celular", "email"]
    success_url = "/AppOdonto/paciente/list"
    
class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    success_url = "/AppOdonto/paciente/list"


# CRUD TURNO

class TurnoList(LoginRequiredMixin, ListView):
    model = Turno
    
class TurnoDetail(LoginRequiredMixin, DetailView):
    model = Turno

class TurnoCreate(LoginRequiredMixin, CreateView):
    model = Turno
    fields = ["paciente", "servicio", "profesional", "fecha", "horario"]
    success_url = "/AppOdonto/turno/list"   

class TurnoUpdate(LoginRequiredMixin, UpdateView):
    model = Turno
    fields = ["paciente", "servicio", "profesional", "fecha", "horario"]
    success_url = "/AppOdonto/turno/list"   

class TurnoDelete(LoginRequiredMixin, DeleteView):
    model = Turno
    success_url = "/AppOdonto/turno/list"
    

# REGISTRO - LOGIN

def registro(request):
    if request.method == "POST":
        miFormulario = RegistroFormulario(request.POST)
        if miFormulario.is_valid():
            #username = miFormulario.cleaned_data['username']
            miFormulario.save()
            return render(request, "AppOdonto/inicio.html", {'mensaje':"Usuario registrado"})
    else:
        miFormulario = RegistroFormulario()
    return render(request, "AppOdonto/autenticacion/registro.html", {"formulario1":miFormulario})

def login_request(request): 
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST) 
        if form.is_valid():
            usuario = form.cleaned_data.get("username") 
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra) 
            if user is not None:
                login(request, user)          
                mensaje = f"Bienvenido {usuario}"
                return render(request, "AppOdonto/inicio.html", {"mensaje":mensaje})
            else:
                mensaje = f"Datos ingresados incorrectos."
                return render(request, "AppOdonto/inicio.html", {"mensaje":mensaje})
    else:
        form = AuthenticationForm()
    return render(request, "AppOdonto/autenticacion/login.html", {"form":form})   

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, "AppOdonto/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    return render(request, "AppOdonto/editarPerfil.html",{"miFormulario":miFormulario, "usuario":usuario})


# CRUD IMAGEN

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar (usuario=usuarioActual, imagen=form.cleaned_data['imagen'])
            avatar.save()
            return render(request, "AppOdonto/inicio.html")
    else:
        form = AvatarFormulario()
    return render(request, "AppOdonto/agregarAvatar.html",{"formulario":form})


# ABOUT

def about(request):
    return render(request, "AppOdonto/about.html")