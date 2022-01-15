from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView)

from django.urls import path, re_path
from homepage.views import (Index, ListaOrganizaciones, detalleOrg, ListaAnimalesTodo, detalleAnim, ListaAnimalesCan,
                            detalleAnimCan, ListaAnimalesGatos, detalleAnimGatos, ListaAnimalesOtros,
                            detalleAnimOtros, EncuentraAtuMascota, ListaAnimOrganizacion)

from homepage.loginRegister.views import registro, login_page, cierreSesion, cambiar_Contrasena

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('inicioSesion/', login_page, name="InicioSesion"),
    path('Registro/', registro, name="Registro"),
    path('logout/', cierreSesion, name="Logout"),
    url(r'^cambioContraseña/$', cambiar_Contrasena, name='CambioContraseña'),
    # ListaOrganizaciones
    path('listaOrganizacion/detalleOrg/<int:id>', detalleOrg, name='DetalleOrganizacion'),
    path('listaOrganizacion/', ListaOrganizaciones.as_view(), name='ListaOrganizaciones'),
    # animales en adopcion:TODOS
    url(r'^animalesenAdopcion/Detalles/(?P<slug>[^/]*)/$', detalleAnim, name='DetalleAnimEnAdop'),
    # path('animalesenAdopcion/detalleAnim/<slug:slug>', detalleAnim, name='DetalleAnimEnAdop'),
    path('animalesenAdopcion/', ListaAnimalesTodo.as_view(), name='ListaAnimalesAdopcion'),
    # animales en adopcion:CANES
    # path('animalesenAdopcionCan/detalleAnimCan/<slug:slug>', detalleAnimCan, name='DetalleEnAdopCan'),
    url(r'^animalesenAdopcionCan/detalleAnimCan/(?P<slug>[^/]*)/$', detalleAnimCan, name='DetalleEnAdopCan'),
    path('animalesenAdopcionCan/', ListaAnimalesCan.as_view(), name='ListaAnimalesAdopcionCan'),
    # animales en adopcion:GATOS
    path('animalesenAdopcionGato/detalleAnimGato/<slug:slug>', detalleAnimGatos, name='DetalleEnAdopGatos'),
    path('animalesenAdopcionGato/', ListaAnimalesGatos.as_view(), name='ListaAnimalesAdopcionGatos'),
    # animales en adopcion:OTROS
    path('animalesenAdopcionOtros/detalleAnimOtros/<slug:slug>', detalleAnimOtros, name='DetalleEnAdopOtros'),
    path('animalesenAdopcionOtros/', ListaAnimalesOtros.as_view(), name='ListaAnimalesAdopcionOtros'),
    # encuentra a tu mascota
    path('encuentraAtuMascota/', EncuentraAtuMascota.as_view(), name='EncuentraAtuMascota'),
    # Lista animales solo organizacion
    path('AOrg/<int:pk>', ListaAnimOrganizacion.as_view(), name='ListAnimOrg'),

    path('reset/password_reset',
         PasswordResetView.as_view(template_name='incioRegistro/RecuperarContraseña/password_reset_form.html',
                                   email_template_name='incioRegistro/RecuperarContraseña/password_reset_email.html'),
         name='password_reset'),
    path('reset/password_reset_done',
         PasswordResetDoneView.as_view(template_name='incioRegistro/RecuperarContraseña/password_reset_done.html'),
         name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$',
            PasswordResetConfirmView.as_view(
                template_name='incioRegistro/RecuperarContraseña/password_reset_confirm.html'),
            name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

]
