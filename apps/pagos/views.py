from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.pagos.models import Pagos
from apps.pagos.forms import PagoForm
from django.urls import reverse_lazy

# Create your views here.

class PagosList(ListView):
    model = Pagos  
    template_name = 'pagos/pago_list.html'
    
class PagoCreate(CreateView): 
    model = Pagos 
    form_class = PagoForm 
    template_name = 'pagos/pago_form.html'
    success_url = reverse_lazy('pagos_listar')

class PagoUpdate(UpdateView):
    model = Pagos
    form_class = PagoForm
    template_name = 'pagos/pago_form.html'
    success_url = reverse_lazy('pagos_listar')

class PagoDelete(DeleteView):
    model = Pagos
    success_url = reverse_lazy('pagos_listar')    
