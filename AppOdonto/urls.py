from django.urls import path
from AppOdonto.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/",inicio, name="Inicio"),    
    
    #Autenticacion de usuario
    path("registro/", registro, name="Registro"),
    path("login/", iniciar_sesion, name="Login"),
    path("logout/", LogoutView.as_view(template_name="AppOdonto/autenticacion/logout.html"),name="Logout"),
    path("about", about, name="About"),

       
    path("profesionales/nuevo", ProfesionalCrear.as_view(), name="Crear Profesional"),
    path("profesionales/ver", ProfesionalVer.as_view(), name="Ver Profesional"),
    path("profesionales/modificar/<int:pk>", ProfesionalModificar.as_view(), name="Modificar Profesional"),
    path("profesionales/eliminar/<int:pk>", ProfesionalEliminar.as_view(), name="Eliminar Profesional"),
    
    path("pacientes/nuevo", PacienteCrear.as_view(), name="Crear Paciente"),
    path("pacientes/ver", PacienteVer.as_view(), name="Ver Paciente"),
    path("pacientes/modificar/<int:pk>", PacienteModificar.as_view(), name="Modificar Paciente"),
    path("pacientes/eliminar/<int:pk>", PacienteEliminar.as_view(), name="Eliminar Paciente"),
    
    path("turnos/nuevo", TurnoCrear.as_view(), name="Crear Turno"),
    path("turnos/ver", TurnoVer.as_view(), name="Ver Turno"),
    path("turnos/modificar/<int:pk>", TurnoModificar.as_view(), name="Modificar Turno"),
    path("turnos/eliminar/<int:pk>", TurnoEliminar.as_view(), name="Eliminar Turno"),    
    
    
    
    
]