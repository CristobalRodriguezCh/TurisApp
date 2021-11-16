from django.contrib import admin
from apps.Persona.models import Persona
from apps.Turista.models import Gustos, Turista

# Register your models here.
class MembershipInline(admin.TabularInline):
    model= Gustos
    extra=1
   

class TuristaAdmin(admin.ModelAdmin):
    inlines= (MembershipInline,)
    list_display=('id','persona_id')
 
    
admin.site.register(Turista,TuristaAdmin)