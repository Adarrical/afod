
from django import forms 
import re
import datetime
from apps.miembro.models import Miembro 
from apps.miembro.models import Historico 

class MiembroForm(forms.ModelForm):

    class Meta:
        model = Miembro 
        fields = "__all__"

    def clean_codigo_postal(self):
        data = self.cleaned_data['codigo_postal']
        patron = re.compile('[0-9]{5}')
        matcher = patron.match(data)
        if (matcher) == False:
            raise forms.ValidationError("Introduzca un código postal válido")
        return data

    year_ini = 1940
    year_fin = datetime.date.today().year - 12 
    fecha_nacimiento = forms.DateField(required=False, 
        widget=forms.SelectDateWidget(years=range(year_fin, year_ini, -1),),
        )   

    year_fin = datetime.date.today().year 
    year_ini = 2017
    fecha_inscripcion = forms.DateField(
        widget=forms.SelectDateWidget(years=range(year_fin,year_ini, -1),),
    )
    
    tipo_miembro = forms.ChoiceField(choices=Miembro.TIPO_MIEMBRO)  
     
    def clean(self): 
        print(self.cleaned_data)
        return self.cleaned_data

class HistoricoForm(forms.ModelForm) :

    class Meta:
        model = Historico 
        fields = "__all__"
        #exclude = ['miembro']

    
    year_ini = 2018
    year_fin = datetime.date.today().year 
    fecha_cobro = forms.DateField(required=True, 
        widget=forms.SelectDateWidget(years=range(year_fin, year_ini, -1),),
    )

    tipo_cobro = forms.ChoiceField(choices=Historico.TIPO_COBRO)  
    
    def clean(self): 
        print(self.cleaned_data)
        return self.cleaned_data
    
class HistoricoFormMember(forms.ModelForm):

    class Meta:
        model = Historico 
        fields = [  'fecha_cobro',
                    'tipo_cobro',
                    'importe', ]
        #widgets = {'miembro':forms.HiddenInput()}
          
    year_ini = 2018
    year_fin = datetime.date.today().year 
    fecha_cobro = forms.DateField(required=True, 
        widget=forms.SelectDateWidget(years=range(year_fin, year_ini, -1),),
    )

    tipo_cobro = forms.ChoiceField(choices=Historico.TIPO_COBRO)  
    
    def clean(self): 
        print(self.cleaned_data)
        return self.cleaned_data
    
        