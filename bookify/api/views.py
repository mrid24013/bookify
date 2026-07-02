from rest_framework import viewsets, permissions
from .models import Espacio, Reservacion
from .serializers import EspacioSerializer, ReservacionSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class EspacioViewSet(viewsets.ModelViewSet):
    queryset = Espacio.objects.filter(activo=True)
    serializer_class = EspacioSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]


class ReservacionViewSet(viewsets.ModelViewSet):
    serializer_class = ReservacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Si es Administrador ve todas las reservas; si es Cliente solo las suyas 
        user = self.request.user
        if user.is_staff:
            return Reservacion.objects.all()
        return Reservacion.objects.filter(usuario=user)

    def perform_create(self, serializer):
        # Asocia automáticamente la reserva al usuario autenticado de Postman
        serializer.save(usuario=self.request.user)