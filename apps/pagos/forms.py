from django import forms 
import datetime
from apps.pagos.models import Pagos 

class PagoForm(forms.ModelForm):

    class Meta:
        model = Pagos
        fields = "__all__"
    
    year_ini = 2018
    year_fin = datetime.date.today().year 
    fecha_pago= forms.DateField(required=True, 
        widget=forms.SelectDateWidget(years=range(year_fin, year_ini, -1),),
    )

    tipo_pago = forms.ChoiceField(choices=Pagos.TIPO_PAGO)  
    
    