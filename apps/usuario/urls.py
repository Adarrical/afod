from django.urls import path
from django.contrib.auth.views import LogoutView
from apps.usuario.views import Login


urlpatterns = [
   path('login', Login.as_view(),name="login"),
   path('logout', LogoutView.as_view(), name="logout"),
]

