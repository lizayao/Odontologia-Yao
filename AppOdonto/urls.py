from django.urls import path
from AppOdonto import views
from AppOdonto.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="Inicio"),    
    
    # CRUD PROFESIONALES
    path('profesional/list/', ProfesionalList.as_view(), name="Profesional List"),
    path('profesional/<int:pk>', ProfesionalDetail.as_view(), name="Profesional Detail"),
    path('profesional/crear/', ProfesionalCreate.as_view(), name="Profesional Create"),
    path('profesional/editar/<int:pk>', ProfesionalUpdate.as_view(), name="Profesional Edit"),
    path('profesional/borrar/<int:pk>', ProfesionalDelete.as_view(), name="Profesional Delete"),    
    
    # CRUD SERVICIOS (con clases)
    path('servicio/list/', ServicioList.as_view(), name="Servicio List"),
    path('servicio/<int:pk>', ServicioDetail.as_view(), name="Servicio Detail"),
    path('servicio/crear/', ServicioCreate.as_view(), name="Servicio Create"),
    path('servicio/editar/<int:pk>', ServicioUpdate.as_view(), name="Servicio Edit"),
    path('servicio/borrar/<int:pk>', ServicioDelete.as_view(), name="Servicio Delete"),
    
    # CRUD PACIENTES (con clases)
    path('paciente/list/', PacienteList.as_view(), name="Paciente List"),
    path('paciente/<int:pk>', PacienteDetail.as_view(), name="Paciente Detail"),   
    path('paciente/crear/', PacienteCreate.as_view(), name="Paciente Create"),
    path('paciente/modificar/<int:pk>', PacienteUpdate.as_view(), name="Paciente Edit"),
    path('paciente/eliminar/<int:pk>', PacienteDelete.as_view(), name="Paciente Delete"),
    
    # CRUD TURNOS (con clases)
    path('turno/list/', TurnoList.as_view(), name="Turno List"),
    path('turno/<int:pk>', TurnoDetail.as_view(), name="Turno Detail"),
    path('turno/crear/', TurnoCreate.as_view(), name="Turno Create"),
    path('turno/modificar/<int:pk>', TurnoUpdate.as_view(), name="Turno Edit"),
    path('turno/eliminar/<int:pk>', TurnoDelete.as_view(), name="Turno Delete"), 
    
    # AUTENTICACION USUARIO
    path("registro/", views.registro, name="Registro"),
    path("login/", views.login_request, name="Login"),
    path("logout/", LogoutView.as_view(template_name="AppOdonto/autenticacion/logout.html"),name="Logout"),
    path("editarPerfil/", views.editarPerfil, name="Editar Perfil"),
    
    # AVATAR
    path("agregarAvatar", views.agregarAvatar, name="Avatar"),
    
    path("about/", about, name="About"),  
       
    
]