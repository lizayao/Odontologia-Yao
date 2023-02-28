from django.contrib import admin
from AppOdonto.models import *

# Register your models here.


admin.site.register(ProfesionalModel)
admin.site.register(ServicioModel)
admin.site.register(PacienteModel)
admin.site.register(TurnoModel)

admin.site.register(AvatarImagen)