from django.urls import path
from AppOdonto.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/",inicio, name="Start"),    
    
    #Autenticacion de usuario
    path("registro/", registro, name="Sign Up"),
    path("login/", iniciar_sesion, name="Sign In"),
    path("logout/", LogoutView.as_view(template_name="AppOdonto/autenticacion/logout.html"),name="Logout"),
         

    
]