from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EspacioViewSet, ReservacionViewSet

router = DefaultRouter()
router.register(r'espacios', EspacioViewSet, basename='espacio')
router.register(r'reservaciones', ReservacionViewSet, basename='reservacion')

urlpatterns = [
    path('', include(router.urls)),
]