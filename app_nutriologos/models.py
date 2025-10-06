from django.db import models

# Create your models here.
class Nutriologo(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    
    # es para el administrador
    def __str__(self):
        return f"{self.nombre}{self.especialidad}"