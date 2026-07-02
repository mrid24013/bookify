from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Espacio, Reservacion

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']


class EspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacio
        fields = '__all__'


class ReservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservacion
        fields = '__all__'
        read_only_fields = ['usuario']

    def validate(self, data):
        espacio = data['espacio']
        fecha = data['fecha']
        hora_inicio = data['hora_inicio']
        hora_fin = data['hora_fin']

        if hora_inicio >= hora_fin:
            raise serializers.ValidationError("La hora de inicio debe ser menor a la hora final.")

        colisiones = Reservacion.objects.filter(
            espacio=espacio,
            fecha=fecha,
            hora_inicio__lt=hora_fin,
            hora_fin__gt=hora_inicio
        )

        if self.instance:
            colisiones = colisiones.exclude(id=self.instance.id)

        if colisiones.exists():
            raise serializers.ValidationError(
                "Este espacio ya se encuentra reservado en el rango seleccionado."
            )

        return data