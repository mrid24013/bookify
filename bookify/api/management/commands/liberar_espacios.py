from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.models import Q
from api.models import Espacio, Reservacion

class Command(BaseCommand):
    help = 'Busca y procesa reservaciones cuya hora de fin ya pasó'

    def handle(self, *args, **kwargs):
        ahora = timezone.localtime()
        hoy = ahora.date()
        hora_actual = ahora.time()

        # Buscar reservaciones pasadas (días anteriores O de hoy cuya hora_fin ya expiró)
        reservaciones_vencidas = Reservacion.objects.filter(
            Q(fecha__lt=hoy) | Q(fecha=hoy, hora_fin__lt=hora_actual)
            # Si le agregaste el campo 'estado' a tu modelo, descomenta la siguiente línea:
            # , estado='ACTIVA'
        )

        cantidad = reservaciones_vencidas.count()

        # Si usas el campo 'estado', actualízalas así:
        # reservaciones_vencidas.update(estado='FINALIZADA')

        self.stdout.write(
            self.style.SUCCESS(f'Se procesaron {cantidad} reservaciones vencidas al momento ({ahora.strftime("%H:%M:%S")}).')
        )