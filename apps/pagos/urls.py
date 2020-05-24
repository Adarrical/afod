from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.pagos.views import PagosList
from apps.pagos.views import PagoCreate
from apps.pagos.views import PagoUpdate
from apps.pagos.views import PagoDelete


urlpatterns = [
    path('', login_required(PagosList.as_view()), name='pagos_listar'),
    path('nuevo', login_required(PagoCreate.as_view()), name='pago_crear'),
    path('<int:pk>/modificar',login_required(PagoUpdate.as_view()), name="pago_modificar"),
    path('<int:pk>/borrar',login_required(PagoDelete.as_view()), name="pago_borrar"),
    
]