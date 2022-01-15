from django.contrib.auth import logout
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from organizacion.models import AnimalesEnAdopcion
from usuario.models import Organizacion


class Index(TemplateView):
    template_name = 'index.html'


class ListaOrganizaciones(ListView):
    model = Organizacion
    context_object_name = 'organizacion_list'
    template_name = 'homepage/ListadoOrg.html'
    queryset = Organizacion.objects.all()
    ordering = ['id']
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ListaOrganizaciones, self).get_context_data(**kwargs)

        context['titulo'] = 'Listado de Organizaciones'
        context['entity'] = 'Listado de Organizaciones'
        context['entity'] = 'Listado de Organizaciones'
        context['entity_url'] = reverse_lazy('index')
        return context


def detalleOrg(request, id):
    organizacion = Organizacion.objects.get(pk=id)
    return render(request, 'homepage/DetallesOrganizaciones.html',
                  {
                      'organizacion': organizacion,
                      'titulo': organizacion.nomorganizacion,
                      'entity': organizacion.nomorganizacion,
                  })


class ListaAnimOrganizacion(ListView):
    model = AnimalesEnAdopcion
    template_name = 'homepage/ListadoAnimales.html'
    ordering = ['id']
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ListaAnimOrganizacion, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        Org = Organizacion.objects.get(id=pk)
        context['especie'] = 'TODO'
        context['object_list'] = AnimalesEnAdopcion.objects.filter(animal__estado='EN ADOPCION').filter(
            animal__organizacion__nomorganizacion=Org.nomorganizacion)
        context['titulo'] = 'Listado de Animales de Compañia en Adopcion'
        context['entity_anterior'] = Org.nomorganizacion
        context['entity_anterior_url'] = reverse('DetalleOrganizacion', args=[pk])
        context['entity'] = 'Listado de Animales de Compañia en Adopcion'


        return context


class ListaAnimalesTodo(ListView):
    model = AnimalesEnAdopcion
    context_object_name = 'animalesAdopcion_list'
    template_name = 'homepage/ListadoAnimales.html'
    queryset = AnimalesEnAdopcion.objects.filter(animal__estado='EN ADOPCION')
    ordering = ['id']
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especie'] = 'TODO'
        context['titulo'] = 'Listado de Animales de Compañia en Adopcion'
        context['entity'] = 'Listado de Animales de Compañia en Adopcion'
        context['entity_url'] = reverse_lazy('ListaAnimalesAdopcion')

        return context


def detalleAnim(request, slug):
    animalenAdop = AnimalesEnAdopcion.objects.get(slug=slug)
    return render(request, 'homepage/DetallesAnimales.html',
                  {
                      'animalenAdop': animalenAdop,
                      'titulo': animalenAdop.animal.nombre,
                      'entity': animalenAdop.animal.nombre,
                      'entity_reverse': 'Listado de animales en Adopcion',
                      'entity_reverse_url': reverse_lazy('ListaAnimalesAdopcion'),
                  })


class ListaAnimalesCan(ListView):
    model = AnimalesEnAdopcion
    context_object_name = 'animalesAdopcionCan_list'
    template_name = 'homepage/ListadoAnimales.html'
    queryset = AnimalesEnAdopcion.objects.filter(animal__especie_id__exact=1).filter(animal__estado='EN ADOPCION')
    ordering = ['id']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especie'] = 'CAN'
        context['titulo'] = 'Listado de Canes en Adopcion '
        context['entity'] = 'Listado de Canes Compañia en Adopcion'
        context['entity_url'] = reverse_lazy('ListaAnimalesAdopcionCan')
        return context


def detalleAnimCan(request, slug):
    animalenAdop = AnimalesEnAdopcion.objects.get(slug=slug)
    return render(request, 'homepage/DetallesAnimales.html',
                  {
                      'animalenAdop': animalenAdop,
                      'titulo': animalenAdop.animal.nombre,
                      'entity': animalenAdop.animal.nombre,
                      'entity_reverse': 'Listado de Canes en adopcion',
                      'entity_reverse_url': reverse_lazy('ListaAnimalesAdopcionCan'),
                  })


class ListaAnimalesGatos(ListView):
    model = AnimalesEnAdopcion
    context_object_name = 'animalesAdopcionCan_list'
    template_name = 'homepage/ListadoAnimales.html'
    queryset = AnimalesEnAdopcion.objects.filter(animal__especie_id__exact=2).filter(animal__estado='EN ADOPCION')
    ordering = ['id']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especie'] = 'GATO'
        context['titulo'] = 'Listado de Gatos en Adopcion '
        context['entity'] = 'Listado de Gatos Compañia en Adopcion'
        context['entity_url'] = reverse_lazy('ListaAnimalesAdopcionGatos')
        return context


def detalleAnimGatos(request, slug):
    animalenAdop = AnimalesEnAdopcion.objects.get(slug=slug)
    return render(request, 'homepage/DetallesAnimales.html',
                  {
                      'animalenAdop': animalenAdop,
                      'titulo': animalenAdop.animal.nombre,
                      'entity': animalenAdop.animal.nombre,
                      'entity_reverse': 'Listado de Gatos en Adopcion',
                      'entity_reverse_url': reverse_lazy('ListaAnimalesAdopcionGatos'),
                  })


class ListaAnimalesOtros(ListView):
    model = AnimalesEnAdopcion
    context_object_name = 'animalesAdopcionCan_list'
    template_name = 'homepage/ListadoAnimales.html'
    queryset = AnimalesEnAdopcion.objects.filter(animal__especie_id=3).filter(animal__estado='EN ADOPCION')
    ordering = ['id']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especie'] = 'OTROS'
        context['titulo'] = 'Listado de Otros Animales en Adopcion '
        context['entity'] = 'Listado de Otros Animales en Adopcion'
        context['entity_url'] = reverse_lazy('ListaAnimalesAdopcionOtros')
        return context


def detalleAnimOtros(request, slug):
    animalenAdop = AnimalesEnAdopcion.objects.get(slug=slug)
    return render(request, 'homepage/DetallesAnimales.html',
                  {
                      'animalenAdop': animalenAdop,
                      'titulo': animalenAdop.animal.nombre,
                      'entity': animalenAdop.animal.nombre,
                      'entity_reverse': 'Listado de otros animales en Adopcion',
                      'entity_reverse_url': reverse_lazy('ListaAnimalesAdopcionOtros'),
                  })


class EncuentraAtuMascota(TemplateView):
    template_name = 'MotorEmparejamiento/InicioMotor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Encuentra a tu mascota'
        context['entity'] = 'Motor de emparejamiento'
        context['entity_url'] = reverse_lazy('EncuentraAtuMascota')
        return context
