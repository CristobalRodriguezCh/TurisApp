from django.contrib import admin

from apps.Maestra.models import Maestra

# Register your models here.

class MaestraAdmn(admin.ModelAdmin):
    list_display=('id','nombre','valor','dependencia')
    search_fields=('nombre','dependencia')
    ordering = ('id','dependencia')
admin.site.register(Maestra,MaestraAdmn)
