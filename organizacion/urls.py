from django.conf.urls import url
from django.urls import path, include
from django import urls
from organizacion.views import (ListaAnimalesTodo, ListaAnimalesRehab, ListaAnimalesEnAdop, ListaAnimalesAdop,
                                ListaAdoptante, ListaAnimalesSantuario)
from organizacion.views import RegistroAnimalesRescatados, detalleAnimalC, detalleAdoptante
from organizacion.views import (PonerEnAdop, RegAdop, animalSantuario)
from organizacion.FormActualizacion.views import (ActualizarAnimEnAdop, ActualizarAnimResc, ActualizardatosBAnim,
                                                  ActualizarRegAdopcion, ActualizarAdoptante, ActualizarEvalRehab,
                                                  ActualizarAnimEnSant)
from organizacion.detalles.views import (detalleDatosBasicos, detalleDatosIngreso, detalleDatosRehab,
                                         detalleDatosEnAdop, detalleDatosAdop, detalleDatosEnSan)

# actualizarEvaluacion
app_name = 'animal'

urlpatterns = [
    #detalles
    url(r'^detAnim/(?P<slug>[^/]*)/$', detalleAnimalC, name='detDatAnim'),
    url(r'^detAnim/datosBasicos/(?P<slug>[^/]*)/$', detalleDatosBasicos, name='detDatAnim(basicos)'),
    url(r'^detAnim/datosIngreso/(?P<slug>[^/]*)/$', detalleDatosIngreso, name='detDatAnim(ingreso)'),
    url(r'^detAnim/datosRehab/(?P<slug>[^/]*)/$', detalleDatosRehab, name='detDatAnim(rehab)'),
    url(r'^detAnim/datosEnAdop/(?P<slug>[^/]*)/$', detalleDatosEnAdop, name='detDatAnim(enAdop)'),
    url(r'^detAnim/datosAdop/(?P<slug>[^/]*)/$', detalleDatosAdop, name='detDatAnim(Adop)'),
    url(r'^detAnim/datosSant/(?P<slug>[^/]*)/$', detalleDatosEnSan, name='detDatAnim(Sant)'),
    url(r'^detAdop/(?P<id>[^/]*)/$', detalleAdoptante, name='detAdoptante'),
    #Registros
    path('RegAnimRes/', RegistroAnimalesRescatados.as_view(), name='RegAnimResc'),
    url(r'^PonerEnAdop/(?P<slug>[^/]*)/$', PonerEnAdop, name='PonerEnAdop'),
    url(r'^RegAdop/(?P<slug>[^/]*)/$', RegAdop, name='RegistrarAdop'),
    url(r'^RegEnSant/(?P<slug>[^/]*)/$', animalSantuario, name='RegistrarEnSant'),
    # path('RegAdopciones/<int:pk>', RegistroAdopcion.as_view(), name='RegistrarAdop'),
    # path('ActDatosAnim/<int:pk>', ActualizardatosBAnim.as_view(), name='ActDatosAnim'),
    #Actualizaciones
    url(r'^ActDatosAnim/(?P<slug>[^/]*)/$', ActualizardatosBAnim.as_view(), name='ActDatosAnim'),
    # path('ActRehab/<int:pk>', ActualizarAnimResc.as_view(), name='ActRehab'),
    url(r'^ActRehab/(?P<slug>[^/]*)/$', ActualizarAnimResc.as_view(), name='ActRehab'),
    url(r'^ActEval/(?P<slug>[^/]*)/$', ActualizarEvalRehab.as_view(), name='ActEval'),
    path('ActEnAdop/<int:pk>', ActualizarAnimEnAdop.as_view(), name='ActEnAdop'),
    path('ActAdop/<int:pk>', ActualizarRegAdopcion.as_view(), name='ActAdop'),
    path('ActAdoptante/<int:pk>', ActualizarAdoptante.as_view(), name='ActAdoptante'),
    path('ActEnSant/<int:pk>', ActualizarAnimEnSant.as_view(), name='ActEnSant'),
    #Listas
    path('ListAnimTod/', ListaAnimalesTodo.as_view(), name='ListaAnimTodo'),
    path('ListAnimEnReha/', ListaAnimalesRehab.as_view(), name='ListaAnimEnRehab'),
    path('ListAnimEnAdop/', ListaAnimalesEnAdop.as_view(), name='ListaAnimEnAdop'),
    path('ListAnimAdop/', ListaAnimalesAdop.as_view(), name='ListaAnimAdop'),
    path('ListAnimSant/', ListaAnimalesSantuario.as_view(), name='ListaAnimEnSant'),
    path('ListAdop/', ListaAdoptante.as_view(), name='ListaAdoptantes'),
]
