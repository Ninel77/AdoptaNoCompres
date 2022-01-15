from django.conf.urls import url
from django.urls import path, include
from django import urls

from MotorEmparejamiento.views import (EncuentraAtuMascota, InfoAlgoritmo, InfoSistema, DatasetLista, AlgEmparejamiento,
                                       detAnimAlg, SistemaRecomendacion, detAnimRecom)
from MotorEmparejamiento.views import createFormCP, createFormSP
from MotorEmparejamiento.views import ActFormCP, ActFormSP

app_name = 'motor'

urlpatterns = [
    path('motEmpIndex/', EncuentraAtuMascota.as_view(), name='InicioMotor'),

    path('InfoAlg/', InfoAlgoritmo, name='InfoAlg'),
    path('InfoSis/', InfoSistema, name= 'InfoSis'),
    path('FormCP/', createFormCP, name='FormCP'),
    path('FormSP/', createFormSP, name='FormSP'),
    # path('ActFormCP/<slug:slug>/', ActFormCP.as_view(), name='ActFormCP'),
    # url(r'^ActFormCP/(?P<slug>[^/]+)$', ActFormCP.as_view(), name='ActFormCP'),
    url(r'^ActFormCP/(?P<slug>[^/]*)/$', ActFormCP.as_view(), name='ActFormCP'),
    url(r'^ActFormSP/(?P<slug>[^/]*)/$', ActFormSP.as_view(), name='ActFormSP'),
    path('ListaDatos/', DatasetLista.as_view(), name='LisData'),
    url(r'^resultadoAlgoritmo/(?P<slug>[^/]*)/$', AlgEmparejamiento.as_view(), name='ResAlgoritmo'),
    url(r'^emparejamiento/Detalles/(?P<slug>[^/]*)/$', detAnimAlg, name='DetalleAnimAE'),

    url(r'^resultadoSistema/(?P<slug>[^/]*)/$', SistemaRecomendacion.as_view(), name='ResRecomendacion'),
    url(r'^emparejamiento/Detalles/(?P<slug>[^/]*)/$', detAnimRecom, name='DetalleAnimSR'),

]
