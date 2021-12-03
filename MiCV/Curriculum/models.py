from django.db import models
from django.utils import timezone


Conocimientos_Ingles = (
    ('nulo','Nulo'),
    ('basico', 'Básico'),
    ('Avanzado','Avanzado'),
)


class CV(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    domicilio = models.CharField(max_length=70)
    localidad = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=80)
    perfil = models.TextField()
    estudios_o_titulos = models.TextField()
    conocimientos_laborales_previos = models.TextField()
    conocimientos_de_ingles = models.CharField(
        max_length=8,
        choices= Conocimientos_Ingles,
        default='Nulo'
    )
def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title