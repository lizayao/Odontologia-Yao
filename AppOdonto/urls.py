from django.urls import path
from AppOdonto import views
from AppOdonto.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/",inicio, name="Inicio"),    
    
    #Autenticacion de usuario
    path("registro/", registro, name="Registro"),
    path("login/", iniciar_sesion, name="Login"),
    path("logout/", LogoutView.as_view(template_name="AppOdonto/autenticacion/logout.html"),name="Logout"),
    path("about/", about, name="About"),  
       
       
    path('profesionalFormulario', profesionalFormulario, name="ProfesionalFormulario"),
       

    
]


       
       
       
    #path("profesionales/nuevo", ProfesionalCrear.as_view(), name="Crear Profesional"),
    #path("profesionales/ver", ProfesionalVer.as_view(), name="Ver Profesional"),
    #path("profesionales/modificar/<int:pk>", ProfesionalModificar.as_view(), name="Modificar Profesional"),
    #path("profesionales/eliminar/<int:pk>", ProfesionalEliminar.as_view(), name="Eliminar Profesional"),
 
 
"""     path("pacientes/paciente/list/", views.PacienteLista.as_view(), name="Lista Paciente"),
    path("pacientes/paciente/detail/", views.PacienteDetalle.as_view(), name="Detalle Paciente"),   
    path("paciente/nuevo/", views.PacienteCrear.as_view(), name="Crear Paciente"),
    path("paciente/modificar/<int:pk>", views.PacienteModificar.as_view(), name="Modificar Paciente"),
    path("paciente/eliminar/<int:pk>", views.PacienteEliminar.as_view(), name="Eliminar Paciente"),
    
   path("turnos/nuevo/", TurnoCrear.as_view(), name="Crear Turno"),
    path("turnos/ver/", TurnoVer.as_view(), name="Ver Turno"),
    path("turnos/modificar/<int:pk>", TurnoModificar.as_view(), name="Modificar Turno"),
    path("turnos/eliminar/<int:pk>", TurnoEliminar.as_view(), name="Eliminar Turno"),  """