from django.db import models

# Create your models here.

class Pagos(models.Model):
    TIPO_PAGO = [
        ('S', 'Servidor'),
        ('C', 'Comisiones'),
        
    ]
    concepto = models.CharField(blank=False, null=False, max_length=50)
    fecha_pago = models.DateField(blank=False, null=False)
    tipo_pago= models.CharField(max_length=1, choices=TIPO_PAGO, blank=False, null=False)
    importe = models.DecimalField(blank=False, max_digits=5, decimal_places=2, default='-', null=False)
        
    def __str__(self):
        return str(self.concepto)  

