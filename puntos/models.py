from django.db import models, transaction
from clientes.models import Cliente
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime 

class Compra(models.Model):
    fecha = models.DateField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    importe_gastado = models.DecimalField(decimal_places=2, default=0, max_digits=10)
    puntos_ganados = models.FloatField(default=0)

    def __str__(self):
        return f'{self.fecha} - {self.cliente.username} - ${self.importe_gastado}'

    def save(self, *args, **kwargs): 
        # asignamos los puntos 1 a 1 con el valor de la compra         
        self.puntos_ganados = float(self.importe_gastado)

        # si es primera vez que se guarda actualizamos los puntos del cliente
        if self.pk is None:
            self.cliente.puntos += self.puntos_ganados
            self.cliente.save()

        super().save(*args, **kwargs)
    

class Recompensa(models.Model):
    nombre = models.CharField(max_length=140, default="")
    descripcion = models.TextField(default="")
    puntos_requeridos = models.FloatField(default=0)
    imagen = models.ImageField(upload_to ='uploads/', blank=True)
    activa = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class TransaccionPunto(models.Model):
    fecha = models.DateField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, blank=True, null=True)
    recompensa = models.ForeignKey(Recompensa, on_delete=models.CASCADE, blank=True, null=True)
    tipos  = (
        ('compra', 'Compra'),
        ('canje', 'Canje'),
	)
    tipo_transaccion = models.CharField(max_length=10, choices=tipos, default="compra")
    cantidad_puntos = models.FloatField(default=0)

    def __str__(self):
        return f'{self.fecha} - {self.cliente.username} - {self.tipo_transaccion}'
    

    def save(self, *args, **kwargs): 
        # al crear una transaccion de tipo canje restamos los puntos al cliente
        if self.pk is None and self.tipo_transaccion=="canje":
            self.cliente.puntos -= self.cantidad_puntos
            self.cliente.save()
        super().save(*args, **kwargs) 


@receiver(post_save, sender=Compra)
def crear_transaccion_compra(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():

            # cuando se registra una compra creamos el registro de los puntos ganados del cliente, para llevar la trazabilidad
            TransaccionPunto.objects.create(
                fecha = datetime.now(),
                cliente = instance.cliente,
                compra = instance,
                tipo_transaccion = "compra",
                cantidad_puntos = instance.puntos_ganados
            )
