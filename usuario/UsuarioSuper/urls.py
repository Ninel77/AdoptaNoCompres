from django.urls import path, include

from usuario.UsuarioSuper.views import (RegistroOrg,ListaOrganizadores,ListaOrganizacion,
                                        ActualizarOrganizacion, ActualizarOrganizador,
                                        ActualizarSuperOrganizador)
app_name = 'superuser'

urlpatterns = [
    path('LisOrg/', ListaOrganizacion.as_view(), name='ListaOrg'),
    path('LisEnOrg/', ListaOrganizadores.as_view(), name='ListaEnOrg'),
    path('RegOrg/', RegistroOrg.as_view(), name='RegiOrg'),
    path('editarOrg/<int:pk>/', ActualizarOrganizacion.as_view(), name='ActOrg'),
    path('editarEncOrg/<int:pk>/', ActualizarOrganizador.as_view(), name='ActEncOrg'),
    path('perfil/<int:pk>/', ActualizarSuperOrganizador.as_view(), name='perfil'),

]