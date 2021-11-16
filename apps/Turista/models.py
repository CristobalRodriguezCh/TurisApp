from django.db import models
from django.db.models.deletion import CASCADE
from apps.Maestra.models import Maestra
from apps.Persona.models import Persona
# Create your models here.
class Turista(models.Model):
    persona = models.ForeignKey(Persona,null=True,blank=True,on_delete=CASCADE)
    actividades= models.ManyToManyField(Maestra,through='Gustos')

class Gustos(models.Model):
    actividades= models.ForeignKey(Maestra,on_delete=CASCADE,limit_choices_to={'dependencia':11})
    turista= models.ForeignKey(Turista,on_delete=CASCADE,related_name='gustos')
    
    class Meta:
        verbose_name='Actividades favoritas' 