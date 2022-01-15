from datetime import datetime, date
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from organizacion.models import (AnimalesDatosB, AnimalesRescatados, AnimalesEnAdopcion,
                                 AnimalesAdoptados, InfoEvaluacion, DocumentosAdopcion,
                                 Adoptante, AnimalesSantuario)

from usuario.models import DatosPersonales


def detalleAnimalC(request, slug):
    print("Ver Detalles")
    animal = None
    animalResc = None
    animalEnAdop = None
    animalAdop = None
    evalM = None
    error = None
    message = None
    message1 = None
    message2 = None
    if AnimalesDatosB.objects.filter(slug=slug).exists():
        print("existe el animal de compania")
        animal = AnimalesDatosB.objects.get(slug=slug)
        # evalM = InfoEvaluacion.objects.get(id=animal.datosMedicos_id)
        # print("eval", type(evalM))
        if AnimalesRescatados.objects.filter(slug=slug).exists():
            print("AnimalesRescatados")
            animalResc = AnimalesRescatados.objects.get(slug=slug)
            if AnimalesEnAdopcion.objects.filter(slug=slug).exists():
                print("Animal En Adopcion")
                animalEnAdop = AnimalesEnAdopcion.objects.get(slug=slug)
                if AnimalesAdoptados.objects.filter(slug=slug).exists():
                    print("Animales adoptados")
                    animalAdop = AnimalesAdoptados.objects.get(slug=slug)
                    if AnimalesAdoptados.objects.filter(slug=slug).exists():
                        print("Animales Santuarios")
                        animalSant = AnimalesSantuario.objects.get(slug=slug)
            else:
                message1 = 'El animal de compañia no esta en Adopcion'
        else:
            error = 'No encontro los datos del animal Rescatado'
    else:
        message = 'No existe Registro del animal de Compañia'

    return render(request, 'animales/DetalleAnimal(Nuevo3).html',
                  {
                      'animal': animal,
                      'animalResc': animalResc,
                      'animalEnAdop': animalEnAdop,
                      'animalAdop': animalAdop,
                      'evalM': evalM,
                      'error': error,
                      'message': message,
                      'message1': message1,
                      'message2': 'Animal de compañia no esta Adoptado',
                      'message3': 'Animal de compañia no esta en Santuario',
                      'titulo': 'Datos Animal de compañia',
                      'titulo1': 'Datos Rescate del animal de compañia',
                      'titulo2': 'Datos en Adopcion del animal de compañia',
                  })


def detalleDatosBasicos(request, slug):
    animal = None
    animalResc = None
    animalEnAdop = None
    animalAdop = None
    animalSant = None
    if AnimalesDatosB.objects.filter(slug=slug).exists():
        animal = AnimalesDatosB.objects.get(slug=slug)
        if AnimalesRescatados.objects.filter(slug=slug).exists():
            animalResc = AnimalesRescatados.objects.get(slug=slug)
    if AnimalesEnAdopcion.objects.filter(slug=slug).exists():
        animalEnAdop = AnimalesEnAdopcion.objects.get(slug=slug)
        if AnimalesAdoptados.objects.filter(slug=slug).exists():
            animalAdop = AnimalesAdoptados.objects.get(slug=slug)
    if AnimalesSantuario.objects.filter(slug=slug).exists():
        animalSant = AnimalesSantuario.objects.get(slug=slug)

    return render(request, 'animales/detalles/datosBasicos.html',
                  {
                      'animal': animal,
                      'animalResc': animalResc,
                      'animalEnAdop': animalEnAdop,
                      'animalAdop': animalAdop,
                      'animalSant': animalSant,
                      'entity': 'Datos Basicos del Animal de compañia',
                      'titulo': animal.nombre,
                      'entity_anterior_url': reverse('animal:ListaAnimTodo'),
                      'entity_anterior': 'Lista de los animales de compañia',
                      'tituloprincipal': 'Datos Basicos',
                      'titulo1': 'Datos Basicos del animal de compañia',
                      'message1': 'El animal de compañia no esta en Adopcion',
                      'message2': 'El animal de compañia no esta Adoptado',
                      'message3': 'El animal de compañia no esta en un Santuario',
                  })


def detalleDatosIngreso(request, slug):
    animal = None
    animalResc = None
    animalEnAdop = None
    animalAdop = None
    animalSant = None
    if AnimalesDatosB.objects.filter(slug=slug).exists():
        animal = AnimalesDatosB.objects.get(slug=slug)
        if AnimalesRescatados.objects.filter(slug=slug).exists():
            animalResc = AnimalesRescatados.objects.get(slug=slug)
    if AnimalesEnAdopcion.objects.filter(slug=slug).exists():
        animalEnAdop = AnimalesEnAdopcion.objects.get(slug=slug)
        if AnimalesAdoptados.objects.filter(slug=slug).exists():
            animalAdop = AnimalesAdoptados.objects.get(slug=slug)
    if AnimalesSantuario.objects.filter(slug=slug).exists():
        animalSant = AnimalesSantuario.objects.get(slug=slug)

    return render(request, 'animales/detalles/ingreso.html',
                  {
                      'animal': animal,
                      'animalResc': animalResc,
                      'animalEnAdop': animalEnAdop,
                      'animalAdop': animalAdop,
                      'animalSant': animalSant,
                      'entity': 'Datos Animal de compañia',
                      'titulo': animal.nombre ,
                      'entity_anterior_url': reverse('animal:ListaAnimEnRehab'),
                      'entity_anterior': 'Lista de animales Ingresados en Rehabilitacion/Observacion',
                      'tituloprincipal': 'Datos Basicos',
                      'titulo1': 'Datos Basicos del animal de compañia',
                      'message1': 'El animal de compañia no esta en Adopcion',
                      'message2': 'El animal de compañia no esta Adoptado',
                      'message3': 'El animal de compañia no esta en un Santuario',
                  })


def detalleDatosRehab(request, slug):
    animal = None
    animalResc = None
    animalEnAdop = None
    animalAdop = None
    animalSant = None
    if AnimalesDatosB.objects.filter(slug=slug).exists():
        animal = AnimalesDatosB.objects.get(slug=slug)
        if AnimalesRescatados.objects.filter(slug=slug).exists():
            animalResc = AnimalesRescatados.objects.get(slug=slug)
    if AnimalesEnAdopcion.objects.filter(slug=slug).exists():
        animalEnAdop = AnimalesEnAdopcion.objects.get(slug=slug)
        if AnimalesAdoptados.objects.filter(slug=slug).exists():
            animalAdop = AnimalesAdoptados.objects.get(slug=slug)
    if AnimalesSantuario.objects.filter(slug=slug).exists():
        animalSant = AnimalesSantuario.objects.get(slug=slug)

    return render(request, 'animales/detalles/rehabilitacion.html',
                  {
                      'animal': animal,
                      'animalResc': animalResc,
                      'animalEnAdop': animalEnAdop,
                      'animalAdop': animalAdop,
                      'animalSant': animalSant,
                      'entity': 'Datos de la evaluación',
                      'titulo': animal.nombre ,
                      'entity_anterior_url': reverse('animal:ListaAnimEnRehab'),
                      'entity_anterior': 'Lista animales Ingresados en Rehabilitacion/Observacion',
                      'tituloprincipal': 'Datos de la evaluación (Rehabilitación)',
                      'message1': 'El animal de compañia no esta en Adopcion',
                      'message2': 'El animal de compañia no esta Adoptado',
                      'message3': 'El animal de compañia no esta en un Santuario',
                  })


def detalleDatosEnAdop(request, slug):
    animal = None
    animalResc = None
    animalEnAdop = None
    animalAdop = None
    animalSant = None
    if AnimalesDatosB.objects.filter(slug=slug).exists():
        animal = AnimalesDatosB.objects.get(slug=slug)
        if AnimalesRescatados.objects.filter(slug=slug).exists():
            animalResc = AnimalesRescatados.objects.get(slug=slug)
    if AnimalesEnAdopcion.objects.filter(slug=slug).exists():
        animalEnAdop = AnimalesEnAdopcion.objects.get(slug=slug)
        if AnimalesAdoptados.objects.filter(slug=slug).exists():
            animalAdop = AnimalesAdoptados.objects.get(slug=slug)
    if AnimalesSantuario.objects.filter(slug=slug).exists():
        animalSant = AnimalesSantuario.objects.get(slug=slug)

    return render(request, 'animales/detalles/paraAdopcion.html',
                  {
                      'animal': animal,
                      'animalResc': animalResc,
                      'animalEnAdop': animalEnAdop,
                      'animalAdop': animalAdop,
                      'animalSant': animalSant,
                      'titulo': animal.nombre ,
                      'entity': 'Datos de la evaluación',
                      'entity_anterior_url': reverse('animal:ListaAnimEnAdop'),
                      'entity_anterior': 'Lista animales en adopcion',
                      'tituloprincipal': 'Datos para poner en adopción',
                      'message1': 'El animal de compañia no esta en Adopcion',
                      'message2': 'El animal de compañia no esta Adoptado',
                      'message3': 'El animal de compañia no esta en un Santuario',
                  })


def detalleDatosAdop(request, slug):
    animal = None
    animalResc = None
    animalEnAdop = None
    animalAdop = None
    animalSant = None
    mensaje1 = None
    mensaje2 = None
    datosPer = None
    carnet = None

    if AnimalesDatosB.objects.filter(slug=slug).exists():
        animal = AnimalesDatosB.objects.get(slug=slug)
        if AnimalesRescatados.objects.filter(slug=slug).exists():
            animalResc = AnimalesRescatados.objects.get(slug=slug)
    if AnimalesEnAdopcion.objects.filter(slug=slug).exists():
        animalEnAdop = AnimalesEnAdopcion.objects.get(slug=slug)
        if AnimalesAdoptados.objects.filter(slug=slug).exists():
            animalAdop = AnimalesAdoptados.objects.get(slug=slug)
    if AnimalesSantuario.objects.filter(slug=slug).exists():
        animalSant = AnimalesSantuario.objects.get(slug=slug)

    if request.method == 'GET':
        print(request.GET.get('carnet'))
        carnet = request.GET.get('carnet')
        slug = request.GET.get('slug')
        if carnet != None:
            if Adoptante.objects.filter(persona__Carnet=carnet).exists():
                mensaje1 = 'Existe el carnet registrado'
                if Adoptante.objects.filter(persona__Carnet=carnet).filter(estado='BUEN ADOPTANTE'):
                    mensaje2 = 'El nro de carnet esta registrado como BUEN ADOPTANTE'
                    datosPer = DatosPersonales.objects.get(Carnet=carnet)
                else:
                    mensaje2 = 'El nro de carnet esta registrado como MAL ADOPTANTE'
            else:
                mensaje1 = 'No se encuentra registrado el carnet'

    return render(request, 'animales/detalles/adopcion.html',
                  {
                      'animal': animal,
                      'animalResc': animalResc,
                      'animalEnAdop': animalEnAdop,
                      'animalAdop': animalAdop,
                      'animalSant': animalSant,
                      'carnetAnt': carnet,
                      'entity': 'Datos de la adopcion',
                      'titulo': animal.nombre ,
                      'entity_anterior_url': reverse('animal:ListaAnimAdop'),
                      'entity_anterior': 'Lista animales Adoptados',
                      'tituloprincipal': 'Datos de la Adopcion',
                      'message1': 'El animal de compañia no esta en Adopcion',
                      'message2': 'El animal de compañia no esta Adoptado',
                      'message3': 'El animal de compañia no esta en un Santuario',
                      'accion3': 'Verificar',
                      'mensaje1': mensaje1,
                      'mensaje2': mensaje2,
                      'datos': datosPer,
                  })


def detalleDatosEnSan(request, slug):
    animal = None
    animalResc = None
    animalEnAdop = None
    animalAdop = None
    animalSant = None
    if AnimalesDatosB.objects.filter(slug=slug).exists():
        animal = AnimalesDatosB.objects.get(slug=slug)
        if AnimalesRescatados.objects.filter(slug=slug).exists():
            animalResc = AnimalesRescatados.objects.get(slug=slug)
    if AnimalesEnAdopcion.objects.filter(slug=slug).exists():
        animalEnAdop = AnimalesEnAdopcion.objects.get(slug=slug)
        if AnimalesAdoptados.objects.filter(slug=slug).exists():
            animalAdop = AnimalesAdoptados.objects.get(slug=slug)
    if AnimalesSantuario.objects.filter(slug=slug).exists():
        animalSant = AnimalesSantuario.objects.get(slug=slug)

    return render(request, 'animales/detalles/santuario.html',
                  {
                      'animal': animal,
                      'animalResc': animalResc,
                      'animalEnAdop': animalEnAdop,
                      'animalAdop': animalAdop,
                      'animalSant': animalSant,
                      'entity': 'Datos de la evaluación',
                      'titulo': animal.nombre ,
                      'entity_anterior_url': reverse('animal:ListaAnimEnSant'),
                      'entity_anterior': 'Lista animales en santuarios o refugios de manera permanente',
                      'tituloprincipal': 'Datos del ingreso del animal registrado permanentemente en un santuario o refugio',
                      'message1': 'El animal de compañia no esta en Adopcion',
                      'message2': 'El animal de compañia no esta Adoptado',
                      'message3': 'El animal de compañia no esta en un Santuario',
                  })
