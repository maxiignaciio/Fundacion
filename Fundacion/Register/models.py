from django.db import models

# Create your models here.
class Cuenta(models.Model):
    usuario = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)
    
    def __str__(self):
        return self.usuario