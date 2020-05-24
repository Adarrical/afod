
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import RedirectView


# Create your views here.
class Login(LoginView): 
    template_name = 'usuario/index.html'

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated: 
            return redirect('miembro_listar')
        return(super().dispatch(request,*args,**kwargs))

class LogoutRedirectView(RedirectView): 
    pattern_name = 'login' 
    
    def dispatch(self,request,*args,**kwargs):
        logout(request)
        return super().dispatch(request,*args,**kwargs)
