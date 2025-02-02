from django.contrib import admin
from .models import Compra, Recompensa, TransaccionPunto


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    readonly_fields = ['puntos_ganados']

@admin.register(Recompensa)
class RecompensaAdmin(admin.ModelAdmin):
    pass

@admin.register(TransaccionPunto)
class TransaccionPuntoAdmin(admin.ModelAdmin):
    pass