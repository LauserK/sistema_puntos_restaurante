from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(UserAdmin):
    readonly_fields = ['fecha_ultima_compra', 'fecha_ultimo_canje']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'cedula', 'telefono', 'email' )}),
        ('Puntos Acumulados', {'fields': ('puntos',  )}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined', 'fecha_ultima_compra', 'fecha_ultimo_canje')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password','first_name','last_name','email', 'cedula','telefono')}),  # Añade tus campos aquí
    )