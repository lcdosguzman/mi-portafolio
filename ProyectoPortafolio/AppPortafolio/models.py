from django.db import models

# Create your models here.
class Tecnologia(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField()
    experiencia = models.IntegerField()
