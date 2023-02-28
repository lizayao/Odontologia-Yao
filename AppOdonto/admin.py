from django.contrib import admin
from AppOdonto.models import *

# Register your models here.


admin.site.register(Profesional)
admin.site.register(Servicio)
admin.site.register(Paciente)
admin.site.register(Turno)

admin.site.register(AvatarImagen)