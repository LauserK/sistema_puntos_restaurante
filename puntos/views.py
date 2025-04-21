from rest_framework import viewsets
from .models import Recompensa
from .serializers import RecompensaSerializer

class RecompensaViewSet(viewsets.ModelViewSet):
    queryset = Recompensa.objects.all().filter(activa=True) # La base de datos de objetos a los que se aplicarán las acciones
    serializer_class = RecompensaSerializer # El serializador a usar