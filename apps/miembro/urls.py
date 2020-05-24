from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.miembro.views import MiembroList, MiembroCreate, MiembroUpdate, MiembroDelete
from apps.miembro.views import HistorialCreate
from apps.miembro.views import HistorialListMember
from apps.miembro.views import CuotaDelete, CuotaUpdate
from apps.miembro.views import HistorialCreateMember

urlpatterns = [
    path('lista/', login_required(MiembroList.as_view()), name='miembro_listar'),
    path('nuevo/', MiembroCreate.as_view(), name = 'miembro_crear'),
    #url(r'^modificar/(?P<pk>\d+)/$', MiembroUpdate.as_view(), name = 'miembro_modificar'),
    path('<int:pk>/modificar', login_required(MiembroUpdate.as_view()), name = 'miembro_modificar'),
    path('<int:pk>/historial/', login_required(HistorialListMember.as_view()), name = 'miembro_historial'),
    path('borrar/<int:pk>/', login_required(MiembroDelete.as_view()), name = 'miembro_borrar'),
    path('cuotas/',login_required(HistorialCreate.as_view()), name="crear_cuota"),  
    path('<int:pk>/historial/cuota/', login_required(HistorialCreateMember.as_view()), name="crear_cuota"),      
    path('<int:pk>/historial/cuota/<int:pk_1>', login_required(CuotaUpdate.as_view()), name="modificar_cuota"),
    path('<int:pk>/historial/cuota/<int:pk_1>/borrar', login_required(CuotaDelete.as_view()), name="borrar_cuota"),
]