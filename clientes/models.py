from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Cliente(AbstractUser):
    cedula = models.CharField(max_length=15)
    telefono = models.CharField(max_length=20, blank=True)
    puntos = models.FloatField(default=0)

    fecha_ultima_compra = models.DateField(blank=True, null=True)
    fecha_ultimo_canje = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username