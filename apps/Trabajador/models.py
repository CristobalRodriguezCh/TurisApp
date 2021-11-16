from django.db import models
from django.db.models.deletion import CASCADE
from apps.Maestra.models import Maestra

from apps.Persona.models import Persona

# Create your models here.
class Trabajador(models.Model):
    persona= models.ForeignKey(Persona,on_delete=CASCADE,null=False,blank=False)
    rol = models.ForeignKey(Maestra,null=True,on_delete=CASCADE,limit_choices_to={'dependencia':10},related_name='rol')
    class Meta:
        verbose_name="Trabajadore"
