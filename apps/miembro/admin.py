from django.contrib import admin
from apps.miembro.models import Miembro
from apps.miembro.models import Historico

# Register your models here.
admin.site.register(Miembro)
admin.site.register(Historico)
