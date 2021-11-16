from django.contrib import admin
from django.db.models.base import Model
from apps.Persona.models import Persona
from apps.Turista.models import Turista

# Register your models here.

admin.site.register(Persona)