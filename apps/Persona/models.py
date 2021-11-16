from typing import Callable
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

from apps.Maestra.models import Maestra

# Create your models here.
class Persona(models.Model):
    nombre  = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    tipo_documento= models.ForeignKey(Maestra,on_delete=CASCADE,limit_choices_to={'dependencia':8},related_name='tipoIden')
    identidad=models.CharField(max_length=11,verbose_name='numero de documento')
    telefono = models.CharField(max_length=11)
    genero = models.ForeignKey(Maestra,on_delete=CASCADE,limit_choices_to={'dependencia':7},related_name='genero')
    nacionalidad =models.ForeignKey(Maestra,null=True,on_delete=CASCADE,limit_choices_to={'dependencia':9},related_name='nacionalidad')
    def __str__(self) -> str:
        return self.nombre+' '+self.apellido

