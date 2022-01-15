from django.urls import path, include

from reportes.Organizacion.General.views import repTotalOrg, repRehabAnimOrg, repEnAdopAnimOrg, repAdopAnimOrg
from reportes.views import IndiceReporte

app_name = 'rep'

urlpatterns = [
    path('superr/', include('reportes.SuperUser.urls')),
    path('Orgg/', include('reportes.Organizacion.urls')),
]
