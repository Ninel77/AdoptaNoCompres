from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, MonthArchiveView, View
from organizacion.models import (AnimalesDatosB, AnimalesRescatados, AnimalesEnAdopcion, AnimalesAdoptados,
                                 AnimalesSantuario)
from usuario.models import Organizacion, Voluntario

class IndiceReporte(TemplateView):
    template_name = 'Reportes/Organizacion/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de reportes'
        context['entity'] = 'Lista de reportes'
        return context