from django.urls import path, include
from django.conf.urls import url


from usuario.Organizacion.views import (ListaVoluntarios, RegVol, ActualizarVoluntario,
                                        PerfilActualizarOrganizador, ActualizarOrganizacion,
                                        ActualizarPerfilVoluntario)
from usuario.views import ActualizarPerfilUsuarioRegistrado

app_name = 'org'

urlpatterns = [
    path('listVol/', ListaVoluntarios.as_view(), name='ListVol'),
    path('RegVol/', RegVol.as_view(), name='RegVol'),
    path('ActVol/<int:pk>/', ActualizarVoluntario.as_view(), name='ActVol'),
    path('perfilOrd/<int:pk>/', PerfilActualizarOrganizador.as_view(), name='perEncargado'),
    #url(r'^ActPerfil/(?P<slug>[^/]*)/$', PerfilActualizarOrganizador.as_view(), name='perEncargado'),
    path('perfilORganizacion/<int:pk>/', ActualizarOrganizacion.as_view(), name='perfilOrg'),
    path('perfilVoluntario/<int:pk>/', ActualizarPerfilVoluntario.as_view(), name='perfilVol'),
    path('perfilUsuarioReg/<int:pk>/', ActualizarPerfilUsuarioRegistrado.as_view(), name='perfilUserReg'),

]