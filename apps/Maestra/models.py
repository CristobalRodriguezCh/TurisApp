from django.db import models
from django.db.models.base import Model

# Create your models here.
class Maestra(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.CharField(max_length=100,null=True,blank=True)
    dependencia = models.CharField(max_length=11,null=True,blank=True)

    def __str__(self):
        return  '({}) {}'.format(self.valor,self.nombre)
    
    

