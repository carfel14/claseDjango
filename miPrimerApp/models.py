from django.db import models

# Create your models here.
class Aeropuerto(models.Model):
    codigo = models.CharField(max_length=3)
    ciudad = models.CharField(max_length=64)

class Vuelo(models.Model):
    origen = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, related_name='salidas')
    destino = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, related_name='llegadas')
    duracion = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.origen} hacia {self.destino}'