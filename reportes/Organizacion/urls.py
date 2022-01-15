from django.urls import path

from reportes.Organizacion.General.views import (repTotalOrg, repRehabAnimOrg, repEnAdopAnimOrg, repAdopAnimOrg,
                                                 repEnSanAnimOrg, RepOrgCantVol)
from reportes.Organizacion.Caninos.views import (CANrepTotalOrg, CANrepRehabAnimOrg, CANrepEnAdopAnimOrg,
                                                 CANrepAdopAnimOrg,CANrepEnSanAnimOrg)
from reportes.Organizacion.Felinos.views import (GATrepTotalOrg, GATrepRehabAnimOrg, GATrepEnAdopAnimOrg,
                                                 GATrepAdopAnimOrg,GATrepEnSanAnimOrg)
from reportes.Organizacion.Otros.views import (OTRrepTotalOrg, OTRrepRehabAnimOrg, OTRrepEnAdopAnimOrg,
                                                 OTRrepAdopAnimOrg,OTRrepEnSanAnimOrg)
from reportes.views import IndiceReporte

app_name = 'reportesOrganizacion'

urlpatterns = [
    # path('inf/', Index.as_view(), name='Indexreport'),
    path('indexReporte/', IndiceReporte.as_view(), name='IndiceRepOrg'),
    # General
    path('GrepGenOrgan/', repTotalOrg, name='GrepOrg(general)'),
    path('GrepIngrOrgan/', repRehabAnimOrg, name='GrepOrg(Ingreso)'),
    path('GrepEnAdopOrgan/', repEnAdopAnimOrg, name='GrepOrg(EnAdop)'),
    path('GrepAdopOrgan/', repAdopAnimOrg, name='GrepOrg(Adop)'),
    path('GrepEnSantOrgan/', repEnSanAnimOrg, name='GrepOrg(EnSant)'),
    # Canes
    path('CrepGenOrgan/', CANrepTotalOrg, name='CrepOrg(general)'),
    path('CrepIngrOrgan/', CANrepRehabAnimOrg, name='CrepOrg(Ingreso)'),
    path('CrepEnAdopOrgan/', CANrepEnAdopAnimOrg, name='CrepOrg(EnAdop)'),
    path('CrepAdopOrgan/', CANrepAdopAnimOrg, name='CrepOrg(Adop)'),
    path('CrepEnSantOrgan/', CANrepEnSanAnimOrg, name='CrepOrg(EnSant)'),
    # Felinos
    path('FrepGenOrgan/', GATrepTotalOrg, name='FrepOrg(general)'),
    path('FrepIngrOrgan/', GATrepRehabAnimOrg, name='FrepOrg(Ingreso)'),
    path('FrepEnAdopOrgan/', GATrepEnAdopAnimOrg, name='FrepOrg(EnAdop)'),
    path('FrepAdopOrgan/', GATrepAdopAnimOrg, name='FrepOrg(Adop)'),
    path('FrepEnSantOrgan/', GATrepEnSanAnimOrg, name='FrepOrg(EnSant)'),
    # Otros
    path('OrepGenOrgan/', OTRrepTotalOrg, name='OrepOrg(general)'),
    path('OrepIngrOrgan/', OTRrepRehabAnimOrg, name='OrepOrg(Ingreso)'),
    path('OrepEnAdopOrgan/', OTRrepEnAdopAnimOrg, name='OrepOrg(EnAdop)'),
    path('OrepAdopOrgan/', OTRrepAdopAnimOrg, name='OrepOrg(Adop)'),
    path('OrepEnSantOrgan/', OTRrepEnSanAnimOrg, name='OrepOrg(EnSant)'),
    # Organizacion
    path('Organ/', RepOrgCantVol, name='Org'),

]
