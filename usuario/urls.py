from django.contrib import admin
from django.urls import path, include
from usuario.views import ActualizarPerfilUsuarioRegistrado

app_name = 'userLog'

urlpatterns = [
    path('super/', include('usuario.UsuarioSuper.urls')),
    path('org/', include('usuario.Organizacion.urls')),
]
