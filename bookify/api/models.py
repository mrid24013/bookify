from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Espacio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    
    @property
    def esta_disponible(self):
        # Obtenemos la fecha y hora actual local
        ahora = timezone.localtime(timezone.now())
        hoy = ahora.date()
        hora_actual = ahora.time()

        # Busca si hay alguna reservación activa hoy en la hora actual
        ocupado = self.reservaciones.filter(
            fecha=hoy,
            hora_inicio__lte=hora_actual,
            hora_fin__gt=hora_actual
        ).exists()
        
        return not ocupado

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