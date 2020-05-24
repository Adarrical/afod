from django.db import models
from django.core.exceptions import ValidationError 
import re

def valida_codigo_postal(value):
    patron = re.compile('[0-9]{5}')
    matcher = patron.match(value)
    if (matcher):
        return value
    else:
        raise ValidationError("Introduzca un código postal válido")

# Create your models here.
class Miembro(models.Model):
    TIPO_MIEMBRO = [
        ('F', 'Fundador'), 
        ('H', 'Socio de honor'), 
        ('P', 'Presidente de honor'),
        ('G', 'General'),
    ]
    nombre = models.CharField(max_length=50, blank=False)
    apellidos = models.CharField(max_length=70, blank = False)
    direccion = models.CharField(max_length=70, blank=False)
    codigo_postal = models.CharField(max_length=5,
                    validators=[valida_codigo_postal])
    localidad = models.CharField(max_length=30, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    email = models.EmailField()
    dni = models.CharField(blank=True,max_length=18)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    nik_od = models.CharField(max_length=20)
    fecha_inscripcion = models.DateField()
    tipo_miembro= models.CharField(max_length=1, choices=TIPO_MIEMBRO)

    def __str__(self):
        return f'{self.nombre} {self.apellidos} ( {self.nik_od} )'

class Historico(models.Model):
    TIPO_COBRO = [
        ('S', 'Socio'),
        ('D', 'Donativo'),
        ('C', 'Colaborador'),
    ]
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    fecha_cobro = models.DateField(blank=False, null=False)
    tipo_cobro = models.CharField(max_length=1, choices=TIPO_COBRO, blank=False, null=False)
    importe = models.DecimalField(blank=False, max_digits=5, decimal_places=2, default='-', null=False)
        
    def __str__(self):
        return str(self.miembro)  

        


