from django.db import models
from django.contrib.auth.models import User

class Espacio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Reservacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservaciones')
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE, related_name='reservaciones')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return f"{self.usuario.username} - {self.espacio.nombre} ({self.fecha})"