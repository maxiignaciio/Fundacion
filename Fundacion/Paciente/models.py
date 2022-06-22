from django.db import models

# Create your models here
class Paciente(models.Model):
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    domicilio = models.TextField()
    fecha_nacimiento = models.TextField(max_length=10)
    
    def __str__(self):
        return self.nombre
