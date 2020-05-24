from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.views.generic import UpdateView 
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.urls import reverse
from apps.miembro.models import Miembro
from apps.miembro.models import Historico
from apps.miembro.forms import MiembroForm
from apps.miembro.forms import HistoricoForm
from apps.miembro.forms import HistoricoFormMember

# Create your views here.
class MiembroList(ListView):
    model = Miembro  
    template_name = 'miembro/miembro_list.html'

class MiembroCreate(CreateView): 
    model = Miembro 
    form_class = MiembroForm 
    template_name = 'miembro/miembro_form.html'
    success_url = reverse_lazy('miembro_listar')

class MiembroUpdate(UpdateView):
    model = Miembro
    form_class = MiembroForm
    template_name = 'miembro/miembro_form.html'
    success_url = reverse_lazy('miembro_listar')

class MiembroDelete(DeleteView):
    model = Miembro
    success_url = reverse_lazy('miembro_listar')

class HistorialListMember(ListView):
    model = Historico
    template_name = 'miembro/historial_list.html'    
    queryset = Historico.objects.all()
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        self.pk= get_object_or_404(Miembro, id=self.kwargs['pk'])
        context['nombre_miembro']=self.pk
        return context 
    
    def get_queryset(self):
        #print('kwars',self.kwargs)
        #print('++++++++++++++++++++++++++++++++++++++++++++++')
        self.pk= get_object_or_404(Miembro, id=self.kwargs['pk'])
        #print(self.pk)
        queryset = Historico.objects.filter(miembro__exact=self.pk)
        return Historico.objects.filter(miembro=self.pk)

class HistorialCreate(CreateView): 
    model = Historico 
    form_class = HistoricoForm
    
    template_name = 'miembro/historial_form.html'
    
    success_url = reverse_lazy('miembro_listar')  
    #success_url=HttpResponseRedirect('')

class HistorialCreateMember(CreateView): 
    model = Historico 
    form_class = HistoricoFormMember
    
    template_name = 'miembro/historial_form_member.html'

    #Controlamos la vuelta a la url
    def get_success_url(self):
       miembro=self.kwargs['pk']
       return reverse_lazy('miembro_historial', kwargs={'pk': miembro})
   
    
    def form_valid(self, form):
       """
       Establece la foreing key en función del parámetro de la url 
       para que funcione, no se debe definir este campo ni en el form 
       ni en el template. 
       Cuando se salva autoáticamente pondrá la clave
       """
       form.instance.miembro = Miembro.objects.get(id = self.kwargs['pk'])
       return super(HistorialCreateMember, self).form_valid(form)


class CuotaUpdate(UpdateView):
    model = Historico
    form_class = HistoricoFormMember
    template_name = 'miembro/historial_form_member.html'
    #success_url = reverse_lazy('miembro_historial')
    pk_url_kwarg = 'pk_1'
    
    def get_success_url(self):
        miembro=self.kwargs['pk']
        return reverse_lazy('miembro_historial', kwargs={'pk': miembro})
    
    def form_valid(self, form):
       """
       Establece la foreing key en función del parámetro de la url 
       para que funcione, no se debe definir este campo ni en el form 
       ni en el template. 
       Cuando se salva autoáticamente pondrá la clave
       """
       form.instance.miembro = Miembro.objects.get(id = self.kwargs['pk'])
       return super(CuotaUpdate, self).form_valid(form)
  
    """  
    def get_queryset(self):
        
        print('++++++++++++++++++++++++++++++++++++++++++++++')
        print('kwars',self.kwargs)
        print('++++++++++++++++++++++++++++++++++++++++++++++')
        print(self.kwargs['pk_1'])
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        queryset = Historico.objects.filter(id__exact = self.kwargs['pk_1'])
        print(queryset)
        print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
        return queryset
    """
class CuotaDelete(DeleteView):
    model = Historico
    success_url = reverse_lazy('miembro_historial')    
    pk_url_kwarg = 'pk_1'  

    def get_success_url(self):
        # if you are passing 'pk' from 'urls' to 'DeleteView' for company
        # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
        #print("----------------------kwargs",self.kwargs)
        miembro=self.kwargs['pk']
    
        return reverse_lazy('miembro_historial', kwargs={'pk': miembro})
    