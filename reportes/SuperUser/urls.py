from django.urls import path

from reportes.Organizacion.General.views import repTotalOrg, repRehabAnimOrg, repEnAdopAnimOrg, repAdopAnimOrg
from reportes.views import IndiceReporte
app_name = 'reportesSuperUser'

urlpatterns = [
    # path('inf/', Index.as_view(), name='Indexreport'),
    path('indexReporte/', IndiceReporte.as_view(), name='IndiceRepOrg'),
    #General
    path('GrepGenOrgan/', repTotalOrg, name='GrepOrg(general)'),
    path('GrepIngrOrgan/', repRehabAnimOrg, name='GrepOrg(Ingreso)'),
    path('GrepEnAdopOrgan/', repEnAdopAnimOrg, name='GrepOrg(EnAdop)'),
    path('GrepAdopOrgan/', repAdopAnimOrg, name='GrepOrg(Adop)'),
    path('GrepEnSantOrgan/', repEnAdopAnimOrg, name='GrepOrg(EnSant)'),
    #Canes
    path('CrepGenOrgan/', repTotalOrg, name='CrepOrg(general)'),
    path('CrepIngrOrgan/', repRehabAnimOrg, name='CrepOrg(Ingreso)'),
    path('CrepEnAdopOrgan/', repEnAdopAnimOrg, name='CrepOrg(EnAdop)'),
    path('CrepAdopOrgan/', repEnAdopAnimOrg, name='CrepOrg(Adop)'),
    path('CrepEnSantOrgan/', repEnAdopAnimOrg, name='CrepOrg(EnSant)'),
    #Felinos
    path('FrepGenOrgan/', repTotalOrg, name='FrepOrg(general)'),
    path('FrepIngrOrgan/', repRehabAnimOrg, name='FrepOrg(Ingreso)'),
    path('FrepEnAdopOrgan/', repEnAdopAnimOrg, name='FrepOrg(EnAdop)'),
    path('FrepAdopOrgan/', repEnAdopAnimOrg, name='FrepOrg(Adop)'),
    path('FrepEnSantOrgan/', repEnAdopAnimOrg, name='FrepOrg(EnSant)'),
    #Otros
    path('OrepGenOrgan/', repTotalOrg, name='OrepOrg(general)'),
    path('OrepIngrOrgan/', repRehabAnimOrg, name='OrepOrg(Ingreso)'),
    path('OrepEnAdopOrgan/', repEnAdopAnimOrg, name='OrepOrg(EnAdop)'),
    path('OrepAdopOrgan/', repEnAdopAnimOrg, name='OrepOrg(Adop)'),
    path('OrepEnSantOrgan/', repEnAdopAnimOrg, name='OrepOrg(EnSant)'),
    #Organizacion
    path('Organ/', repEnAdopAnimOrg, name='Org'),

]
