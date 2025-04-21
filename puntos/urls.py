from django.urls import path, include
from .views import RecompensaViewSet
from rest_framework.routers import DefaultRouter

# Crea una instancia del Router
router = DefaultRouter()

# Registra tu Viewset con un prefijo de URL (por ejemplo, 'recompensas')
router.register(r'recompensas', RecompensaViewSet, basename='recompensa')

# Las URLs generadas por el router
urlpatterns = [
    path('', include(router.urls)),
]