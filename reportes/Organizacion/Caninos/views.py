from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, MonthArchiveView, View
from organizacion.models import (AnimalesDatosB, AnimalesRescatados, AnimalesEnAdopcion, AnimalesAdoptados,
                                 AnimalesSantuario)
from usuario.models import Organizacion, Voluntario


def CANrepTotalOrg(request):
    nOrg = request.user.voluntario_perfil.organizacion.nomorganizacion

    tAni = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(especie__especies='CANINA').filter(
        especie__especies='CANINA').count()
    tAnIngre = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(
        especie__especies='CANINA').filter(estado='REHABILITACION').count()
    tAnEnAdop = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(
        especie__especies='CANINA').filter(estado='EN ADOPCION').count()
    tAnAdop = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(
        especie__especies='CANINA').filter(estado='ADOPTADO').count()
    tAnEnSant = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(
        especie__especies='CANINA').filter(estado='SANTUARIO').count()

    tEspC = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(especie__especies='CANINA').filter(
        especie__especies__icontains='CANINA').count()
    tEspF = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(especie__especies='CANINA').filter(
        especie__especies__icontains='FELINA').count()
    tEspO = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(especie__especies='CANINA').filter(
        especie__especies__icontains='OTRO').count()

    tTamP = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(especie__especies='CANINA').filter(
        tamano='PEQUEÑO').count()
    tTamM = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(especie__especies='CANINA').filter(
        tamano='MEDIANO').count()
    tTamG = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(especie__especies='CANINA').filter(
        tamano='GRANDE').count()
    tTamGG = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(
        especie__especies='CANINA').filter(tamano='GIGANTE').count()

    tSexF = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(especie__especies='CANINA').filter(
        sexo='HEMBRA').count()
    tSexM = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=nOrg).filter(especie__especies='CANINA').filter(
        sexo='MACHO').count()

    tGestIn = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__gestacion=True).count()
    tLacIn = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__lactancia=True).count()
    tGestEnAdop = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__gestacion=True).count()
    tLacEnAdop = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__lactancia=True).count()
    tGestAdop = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__gestacion=True).count()
    tLacAdop = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__lactancia=True).count()
    tGestEnSant = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__gestacion=True).count()
    tLacEnSant = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__lactancia=True).count()

    tEstFIn = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__sexo='HEMBRA').filter(datosMedicos__esterilizacion=True).count()
    tEstMIn = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__sexo='MACHO').filter(datosMedicos__esterilizacion=True).count()
    tEstFEnAdop = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__sexo='HEMBRA').filter(datosMedicos__esterilizacion=True).count()
    tEstMEnAdop = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__sexo='MACHO').filter(datosMedicos__esterilizacion=True).count()
    tEstFAdop = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__sexo='HEMBRA').filter(datosMedicos__esterilizacion=True).count()
    tEstMAdop = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__sexo='MACHO').filter(datosMedicos__esterilizacion=True).count()
    tEstFEnSant = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__sexo='HEMBRA').filter(datosMedicos__esterilizacion=True).count()
    tEstMEnSant = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__sexo='MACHO').filter(datosMedicos__esterilizacion=True).count()

    return render(request, 'Reportes/Organizacion/detalles/Todo.html',
                  {
                      'nav': 'Caninos',
                      'entity_anterior_url': reverse_lazy('rep:reportesOrganizacion:IndiceRepOrg'),
                      'entity_anterior': 'Lista de Reportes',
                      'entity': 'Reporte acerca de la  Especie Canina (Perros)',
                      'titulo': 'Reporte acerca de la  Especie Canina (Perros)',
                      'tituloprincipal': 'Informacion General de los animales de compañia registrados',
                      'tituloUno': 'Cantidad total de animales de compañia registrados',
                      'tAni': tAni, 'tAnIngre': tAnIngre, 'tAnEnAdop': tAnEnAdop, 'tAnAdop': tAnAdop,
                      'tAnEnSant': tAnEnSant,
                      'tituloDos': 'None',

                      'tituloTres': 'Cantidad total de animales registrados segun Tamaño',
                      'tTamP': tTamP, 'tTamM': tTamM, 'tTamG': tTamG, 'tTamGG': tTamGG,
                      'tituloCuatro': 'Cantidad total de animales registrados segun Genero',
                      'tSexF': tSexF, 'tSexM': tSexM,
                      'tituloCinco': 'Cantidad total de animales registrados segun estado de Gestacion y Lactancia',
                      'tGestIn': tGestIn, 'tGestEnAdop': tGestEnAdop, 'tGestAdop': tGestAdop,
                      'tGestEnSant': tGestEnSant,
                      'tLacIn': tLacIn, 'tLacEnAdop': tLacEnAdop, 'tLacAdop': tLacAdop, 'tLacEnSant': tLacEnSant,
                      'tituloSeis': 'Cantidad total de animales registrados segun estado de Esterilizacion/Castracion',
                      'tEstFIn': tEstFIn, 'tEstMIn': tEstMIn, 'tEstFEnAdop': tEstFEnAdop, 'tEstMEnAdop': tEstMEnAdop,
                      'tEstFAdop': tEstFAdop, 'tEstMAdop': tEstMAdop, 'tEstFEnSant': tEstFEnSant,
                      'tEstMEnSant': tEstMEnSant,
                  })


def CANrepRehabAnimOrg(request):
    nOrg = request.user.voluntario_perfil.organizacion.nomorganizacion

    # para lod de ingreso
    tingreso1 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RESCATE').count()
    ingreso1 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RESCATE').filter(animal__estado='REHABILITACION').count()
    tingreso2 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='NACIDO EN LA ORGANIZACIÓN').count()
    ingreso2 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='NACIDO EN LA ORGANIZACIÓN').filter(animal__estado='REHABILITACION').count()
    tingreso3 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='ABANDONO EN CAMPAÑA/FERIA').count()
    ingreso3 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='ABANDONO EN CAMPAÑA/FERIA').filter(animal__estado='REHABILITACION').count()
    tingreso4 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RECEPCION EN CAMPAÑA/FERIA').count()
    ingreso4 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RECEPCION EN CAMPAÑA/FERIA').filter(animal__estado='REHABILITACION').count()
    tingreso5 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='AYUDA PARA ENCONTRAR HOGAR').count()
    ingreso5 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='AYUDA PARA ENCONTRAR HOGAR').filter(animal__estado='REHABILITACION').count()
    tingreso6 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='OTRO').count()
    ingreso6 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='OTRO').filter(animal__estado='REHABILITACION').count()

    tedad1 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').count()
    edad1 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(animal__estado='REHABILITACION').count()
    tedad2 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').count()
    edad2 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(animal__estado='REHABILITACION').count()
    tedad3 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').count()
    edad3 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(animal__estado='REHABILITACION').count()
    tedad4 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').count()
    edad4 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(
        animal__estado='REHABILITACION').count()
    tedad5 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').count()
    edad5 = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(animal__estado='REHABILITACION').count()

    tin1CL = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RESCATE').filter(edad_Anim='CACHORRO LACTANTE').count()
    tin1C = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RESCATE').filter(edad_Anim='CACHORRO').count()
    tin1J = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RESCATE').filter(edad_Anim='JOVEN').count()
    tin1A = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RESCATE').filter(edad_Anim='ADULTO').count()
    tin1AS = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RESCATE').filter(edad_Anim='ADULTO SENIOR').count()
    tin2CL = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='NACIDO EN LA ORGANIZACIÓN').filter(edad_Anim='CACHORRO LACTANTE').count()
    tin2C = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='NACIDO EN LA ORGANIZACIÓN').filter(edad_Anim='CACHORRO').count()
    tin2J = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='NACIDO EN LA ORGANIZACIÓN').filter(edad_Anim='JOVEN').count()
    tin2A = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='NACIDO EN LA ORGANIZACIÓN').filter(edad_Anim='ADULTO').count()
    tin2AS = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='NACIDO EN LA ORGANIZACIÓN').filter(edad_Anim='ADULTO SENIOR').count()
    tin3CL = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='ABANDONO EN CAMPAÑA/FERIA').filter(edad_Anim='CACHORRO LACTANTE').count()
    tin3C = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='ABANDONO EN CAMPAÑA/FERIA').filter(edad_Anim='CACHORRO').count()
    tin3J = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='ABANDONO EN CAMPAÑA/FERIA').filter(edad_Anim='JOVEN').count()
    tin3A = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='ABANDONO EN CAMPAÑA/FERIA').filter(edad_Anim='ADULTO').count()
    tin3AS = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='ABANDONO EN CAMPAÑA/FERIA').filter(edad_Anim='ADULTO SENIOR').count()
    tin4CL = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RECEPCION EN CAMPAÑA/FERIA').filter(edad_Anim='CACHORRO LACTANTE').count()
    tin4C = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RECEPCION EN CAMPAÑA/FERIA').filter(edad_Anim='CACHORRO').count()
    tin4J = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RECEPCION EN CAMPAÑA/FERIA').filter(edad_Anim='JOVEN').count()
    tin4A = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RECEPCION EN CAMPAÑA/FERIA').filter(edad_Anim='ADULTO').count()
    tin4AS = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RECEPCION EN CAMPAÑA/FERIA').filter(edad_Anim='ADULTO SENIOR').count()
    tin5CL = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='AYUDA PARA ENCONTRAR HOGAR').filter(edad_Anim='CACHORRO LACTANTE').count()
    tin5C = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='AYUDA PARA ENCONTRAR HOGAR').filter(edad_Anim='CACHORRO').count()
    tin5J = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='AYUDA PARA ENCONTRAR HOGAR').filter(edad_Anim='JOVEN').count()
    tin5A = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='AYUDA PARA ENCONTRAR HOGAR').filter(edad_Anim='ADULTO').count()
    tin5AS = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='AYUDA PARA ENCONTRAR HOGAR').filter(edad_Anim='ADULTO SENIOR').count()
    tin6CL = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='OTRO').filter(edad_Anim='CACHORRO LACTANTE').count()
    tin6C = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='OTRO').filter(edad_Anim='CACHORRO').count()
    tin6J = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='OTRO').filter(edad_Anim='JOVEN').count()
    tin6A = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='OTRO').filter(edad_Anim='ADULTO').count()
    tin6AS = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='OTRO').filter(edad_Anim='ADULTO SENIOR').count()

    in1CL = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RESCATE').filter(edad_Anim='CACHORRO LACTANTE').filter(animal__estado='REHABILITACION').count()
    in1C = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RESCATE').filter(edad_Anim='CACHORRO').filter(animal__estado='REHABILITACION').count()
    in1J = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RESCATE').filter(edad_Anim='JOVEN').filter(animal__estado='REHABILITACION').count()
    in1A = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RESCATE').filter(edad_Anim='ADULTO').filter(animal__estado='REHABILITACION').count()
    in1AS = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RESCATE').filter(edad_Anim='ADULTO SENIOR').filter(animal__estado='REHABILITACION').count()
    in2CL = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='NACIDO EN LA ORGANIZACIÓN').filter(edad_Anim='CACHORRO LACTANTE').filter(
        animal__estado='REHABILITACION').count()
    in2C = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='NACIDO EN LA ORGANIZACIÓN').filter(edad_Anim='CACHORRO').filter(
        animal__estado='REHABILITACION').count()
    in2J = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='NACIDO EN LA ORGANIZACIÓN').filter(edad_Anim='JOVEN').filter(
        animal__estado='REHABILITACION').count()
    in2A = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='NACIDO EN LA ORGANIZACIÓN').filter(edad_Anim='ADULTO').filter(
        animal__estado='REHABILITACION').count()
    in2AS = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='NACIDO EN LA ORGANIZACIÓN').filter(edad_Anim='ADULTO SENIOR').filter(
        animal__estado='REHABILITACION').count()
    in3CL = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='ABANDONO EN CAMPAÑA/FERIA').filter(edad_Anim='CACHORRO LACTANTE').filter(
        animal__estado='REHABILITACION').count()
    in3C = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='ABANDONO EN CAMPAÑA/FERIA').filter(edad_Anim='CACHORRO').filter(
        animal__estado='REHABILITACION').count()
    in3J = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='ABANDONO EN CAMPAÑA/FERIA').filter(edad_Anim='JOVEN').filter(
        animal__estado='REHABILITACION').count()
    in3A = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='ABANDONO EN CAMPAÑA/FERIA').filter(edad_Anim='ADULTO').filter(
        animal__estado='REHABILITACION').count()
    in3AS = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='ABANDONO EN CAMPAÑA/FERIA').filter(edad_Anim='ADULTO SENIOR').filter(
        animal__estado='REHABILITACION').count()
    in4CL = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RECEPCION EN CAMPAÑA/FERIA').filter(edad_Anim='CACHORRO LACTANTE').filter(
        animal__estado='REHABILITACION').count()
    in4C = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RECEPCION EN CAMPAÑA/FERIA').filter(edad_Anim='CACHORRO').filter(
        animal__estado='REHABILITACION').count()
    in4J = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RECEPCION EN CAMPAÑA/FERIA').filter(edad_Anim='JOVEN').filter(
        animal__estado='REHABILITACION').count()
    in4A = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RECEPCION EN CAMPAÑA/FERIA').filter(edad_Anim='ADULTO').filter(
        animal__estado='REHABILITACION').count()
    in4AS = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='RECEPCION EN CAMPAÑA/FERIA').filter(edad_Anim='ADULTO SENIOR').filter(
        animal__estado='REHABILITACION').count()
    in5CL = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='AYUDA PARA ENCONTRAR HOGAR').filter(edad_Anim='CACHORRO LACTANTE').filter(
        animal__estado='REHABILITACION').count()
    in5C = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='AYUDA PARA ENCONTRAR HOGAR').filter(edad_Anim='CACHORRO').filter(
        animal__estado='REHABILITACION').count()
    in5J = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='AYUDA PARA ENCONTRAR HOGAR').filter(edad_Anim='JOVEN').filter(
        animal__estado='REHABILITACION').count()
    in5A = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='AYUDA PARA ENCONTRAR HOGAR').filter(edad_Anim='ADULTO').filter(
        animal__estado='REHABILITACION').count()
    in5AS = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='AYUDA PARA ENCONTRAR HOGAR').filter(edad_Anim='ADULTO SENIOR').filter(
        animal__estado='REHABILITACION').count()
    in6CL = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='OTRO').filter(edad_Anim='CACHORRO LACTANTE').filter(animal__estado='REHABILITACION').count()
    in6C = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='OTRO').filter(edad_Anim='CACHORRO').filter(animal__estado='REHABILITACION').count()
    in6J = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='OTRO').filter(edad_Anim='JOVEN').filter(animal__estado='REHABILITACION').count()
    in6A = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='OTRO').filter(edad_Anim='ADULTO').filter(animal__estado='REHABILITACION').count()
    in6AS = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        tipoIngreso='OTRO').filter(edad_Anim='ADULTO SENIOR').filter(animal__estado='REHABILITACION').count()

    return render(request, 'Reportes/Organizacion/detalles/Ingreso.html',
                  {
                      'nav': 'Caninos',
                      'entity_anterior_url': reverse_lazy('rep:reportesOrganizacion:IndiceRepOrg'),
                      'entity_anterior': 'Lista de Reportes',
                      'entity': 'Reporte acerca de la  Especie Canina (Perros)',
                      'titulo': 'Reporte acerca de la  Especie Canina (Perros)',
                      'tituloprincipal': 'Informacion General de los animales ingresados En rehabilitacion/observacion',
                      'tituloUno': 'Cantidad Total Registrada segun Tipo de Ingreso',
                      'tingreso1': tingreso1, 'tingreso2': tingreso2, 'tingreso3': tingreso3, 'tingreso4': tingreso4,
                      'tingreso5': tingreso5, 'tingreso6': tingreso6,
                      'tituloDos': 'Cantidad Total Resgistrada segun Rando de edad del animal',
                      'tedad1': tedad1, 'tedad2': tedad2, 'tedad3': tedad3, 'tedad4': tedad4, 'tedad5': tedad5,
                      'tituloTres': 'Cantidad Total de los animales de ingreso en rehabilitacion/observacion segun Tipo de Ingreso y Rango de edad',
                      'tin1CL': tin1CL, 'tin1C': tin1C, 'tin1J': tin1J, 'tin1A': tin1A, 'tin1AS': tin1AS,
                      'tin2CL': tin2CL, 'tin2C': tin2C, 'tin2J': tin2J, 'tin2A': tin2A, 'tin2AS': tin2AS,
                      'tin3CL': tin3CL, 'tin3C': tin3C, 'tin3J': tin3J, 'tin3A': tin3A, 'tin3AS': tin3AS,
                      'tin4CL': tin4CL, 'tin4C': tin4C, 'tin4J': tin4J, 'tin4A': tin4A, 'tin4AS': tin4AS,
                      'tin5CL': tin5CL, 'tin5C': tin5C, 'tin5J': tin5J, 'tin5A': tin5A, 'tin5AS': tin5AS,
                      'tin6CL': tin6CL, 'tin6C': tin6C, 'tin6J': tin6J, 'tin6A': tin6A, 'tin6AS': tin6AS,
                      'tituloCuatro': 'Cantidad Actual de los animales de ingreso en rehabilitacion/observacion segun Tipo de Ingreso',
                      'ingreso1': ingreso1, 'ingreso2': ingreso2, 'ingreso3': ingreso3, 'ingreso4': ingreso4,
                      'ingreso5': ingreso5, 'ingreso6': ingreso6,
                      'tituloCinco': 'Cantidad Actual de los animales de ingreso en rehabilitacion/observacion segun Rango de edad',
                      'edad1': edad1, 'edad2': edad2, 'edad3': edad3, 'edad4': edad4, 'edad5': edad5,
                      'tituloSeis': 'Cantidad Total de los animales de ingreso en rehabilitacion/observacion segun Tipo de Ingreso y Rango de edad',
                      'in1CL': in1CL, 'in1C': in1C, 'in1J': in1J, 'in1A': in1A, 'in1AS': in1AS,
                      'in2CL': in2CL, 'in2C': in2C, 'in2J': in2J, 'in2A': in2A, 'in2AS': in2AS,
                      'in3CL': in3CL, 'in3C': in3C, 'in3J': in3J, 'in3A': in3A, 'in3AS': in3AS,
                      'in4CL': in4CL, 'in4C': in4C, 'in4J': in4J, 'in4A': in4A, 'in4AS': in4AS,
                      'in5CL': in5CL, 'in5C': in5C, 'in5J': in5J, 'in5A': in5A, 'in5AS': in5AS,
                      'in6CL': in6CL, 'in6C': in6C, 'in6J': in6J, 'in6A': in6A, 'in6AS': in6AS,
                  })


def CANrepEnAdopAnimOrg(request):
    nOrg = request.user.voluntario_perfil.organizacion.nomorganizacion

    tedad1 = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').count()
    edad1 = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(animal__estado='EN ADOPCION').count()
    tedad2 = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').count()
    edad2 = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(
        animal__estado='EN ADOPCION').count()
    tedad3 = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').count()
    edad3 = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(
        animal__estado='EN ADOPCION').count()
    tedad4 = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').count()
    edad4 = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(
        animal__estado='EN ADOPCION').count()
    tedad5 = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').count()
    edad5 = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(animal__estado='EN ADOPCION').count()

    tEsF = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').count()
    tEsM = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').count()

    tEsFCL = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').filter(
        edad_Anim='CACHORRO LACTANTE').count()
    tEsMCL = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').filter(
        edad_Anim='CACHORRO LACTANTE').count()
    tEsFC = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').filter(
        edad_Anim='CACHORRO').count()
    tEsMC = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').filter(
        edad_Anim='CACHORRO').count()
    tEsFJ = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').filter(
        edad_Anim='JOVEN').count()
    tEsMJ = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').filter(
        edad_Anim='JOVEN').count()
    tEsFA = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').filter(
        edad_Anim='ADULTO').count()
    tEsMA = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').filter(
        edad_Anim='ADULTO').count()
    tEsFAS = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').filter(
        edad_Anim='ADULTO SENIOR').count()
    tEsMAS = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').filter(
        edad_Anim='ADULTO SENIOR').count()

    EsF = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').filter(animal__estado='EN ADOPCION').count()
    EsM = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').filter(animal__estado='EN ADOPCION').count()

    EsFCL = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(animal__estado='EN ADOPCION').count()
    EsMCL = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').filter(
        edad_Anim='CACHORRO LACTANTE').filter(animal__estado='EN ADOPCION').count()
    EsFC = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').filter(
        edad_Anim='CACHORRO').filter(animal__estado='EN ADOPCION').count()
    EsMC = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').filter(
        edad_Anim='CACHORRO').filter(animal__estado='EN ADOPCION').count()
    EsFJ = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').filter(
        edad_Anim='JOVEN').filter(animal__estado='EN ADOPCION').count()
    EsMJ = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').filter(
        edad_Anim='JOVEN').filter(animal__estado='EN ADOPCION').count()
    EsFA = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').filter(
        edad_Anim='ADULTO').filter(animal__estado='EN ADOPCION').count()
    EsMA = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').filter(
        edad_Anim='ADULTO').filter(animal__estado='EN ADOPCION').count()
    EsFAS = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').filter(
        edad_Anim='ADULTO SENIOR').filter(animal__estado='EN ADOPCION').count()
    EsMAS = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').filter(
        edad_Anim='ADULTO SENIOR').filter(animal__estado='EN ADOPCION').count()

    return render(request, 'Reportes/Organizacion/detalles/EnAdop.html',
                  {
                      'nav': 'Caninos',
                      'entity_anterior_url': reverse_lazy('rep:reportesOrganizacion:IndiceRepOrg'),
                      'entity_anterior': 'Lista de Reportes',
                      'entity': 'Reporte acerca de la  Especie Canina (Perros)',
                      'titulo': 'Reporte acerca de la  Especie Canina (Perros)',
                      'tituloprincipal': 'Informacion General de los animales en Adopcion',
                      'tituloUno': 'Cantidad Total Registrada por Rango de edad del animal',
                      'tedad1': tedad1, 'tedad2': tedad2, 'tedad3': tedad3, 'tedad4': tedad4, 'tedad5': tedad5,
                      'tituloDos': 'Cantidad Total Registrada de esterilizaciones/Castraciones segun Genero',
                      'tEsF': tEsF, 'tEsM': tEsM,
                      'tEsFCL': tEsFCL, 'tEsMCL': tEsMCL, 'tEsFC': tEsFC, 'tEsMC': tEsMC, 'tEsFJ': tEsFJ,
                      'tEsMJ': tEsMJ, 'tEsFA': tEsFA, 'tEsMA': tEsMA, 'tEsFAS': tEsFAS, 'tEsMAS': tEsMAS,
                      'tituloTres': 'Cantidad Actual de animales en adopcion esterelizadas/castradas segun Rango de edad',
                      'edad1': edad1, 'edad2': edad2, 'edad3': edad3, 'edad4': edad4, 'edad5': edad5,
                      'tituloCuatro': 'Cantidad Actual de animales en adopcion esterelizadas/castradas segun genero',
                      'EsF': EsF, 'EsM': EsM,
                      'EsFCL': EsFCL, 'EsMCL': EsMCL, 'EsFC': EsFC, 'EsMC': EsMC, 'EsFJ': EsFJ,
                      'EsMJ': EsMJ, 'EsFA': EsFA, 'EsMA': EsMA, 'EsFAS': EsFAS, 'EsMAS': EsMAS,
                  })


def CANrepAdopAnimOrg(request):
    nOrg = request.user.voluntario_perfil.organizacion.nomorganizacion

    tedad1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').count()
    tedad2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').count()
    tedad3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').count()
    tedad4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').count()
    tedad5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').count()

    tEsF = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='HEMBRA').count()
    tEsM = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__esterilizacion=True).filter(animal__sexo='MACHO').count()
    tGF = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__gestacion=True).filter(animal__sexo='HEMBRA').count()
    tLF = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__lactancia=True).filter(animal__sexo='HEMBRA').count()

    Vcl1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__tipo_vivienda='CASA PROPIA').count()
    Vcl2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__tipo_vivienda='CASA ALQUILER').count()
    Vcl3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__tipo_vivienda='DEPARTAMENTO PROPIO').count()
    Vcl4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__tipo_vivienda='DEPARTAMENTO ALQUILADO').count()
    Vcl5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__tipo_vivienda='GARZONIER').count()
    Vcl6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__tipo_vivienda='OTRO').count()
    Vc1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__tipo_vivienda='CASA PROPIA').count()
    Vc2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__tipo_vivienda='CASA ALQUILER').count()
    Vc3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__tipo_vivienda='DEPARTAMENTO PROPIO').count()
    Vc4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__tipo_vivienda='DEPARTAMENTO ALQUILADO').count()
    Vc5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__tipo_vivienda='GARZONIER').count()
    Vc6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__tipo_vivienda='OTRO').count()
    Vj1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__tipo_vivienda='CASA PROPIA').count()
    Vj2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__tipo_vivienda='CASA ALQUILER').count()
    Vj3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__tipo_vivienda='DEPARTAMENTO PROPIO').count()
    Vj4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__tipo_vivienda='DEPARTAMENTO ALQUILADO').count()
    Vj5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__tipo_vivienda='GARZONIER').count()
    Vj6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__tipo_vivienda='OTRO').count()
    VA1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__tipo_vivienda='CASA PROPIA').count()
    VA2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__tipo_vivienda='CASA ALQUILER').count()
    VA3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__tipo_vivienda='DEPARTAMENTO PROPIO').count()
    VA4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__tipo_vivienda='DEPARTAMENTO ALQUILADO').count()
    VA5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__tipo_vivienda='GARZONIER').count()
    VA6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__tipo_vivienda='OTRO').count()
    VAS1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__tipo_vivienda='CASA PROPIA').count()
    VAS2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__tipo_vivienda='CASA ALQUILER').count()
    VAS3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__tipo_vivienda='DEPARTAMENTO PROPIO').count()
    VAS4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__tipo_vivienda='DEPARTAMENTO ALQUILADO').count()
    VAS5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__tipo_vivienda='GARZONIER').count()
    VAS6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__tipo_vivienda='OTRO').count()

    Ecl1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__rangoEdad='ADOLECENTE').count()
    Ecl2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__rangoEdad='JOVEN').count()
    Ecl3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__rangoEdad='ADULTO JOVEN').count()
    Ecl4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__rangoEdad='ADULTEZ PRIMARIA').count()
    Ecl5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__rangoEdad='ADULTEZ INTERMEDIA').count()
    Ecl6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__rangoEdad='ADULTEZ TARDIA').count()
    Ecl7 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__rangoEdad='ADULTO MAYOR').count()
    Ec1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__rangoEdad='ADOLECENTE').count()
    Ec2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__rangoEdad='JOVEN').count()
    Ec3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__rangoEdad='ADULTO JOVEN').count()
    Ec4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__rangoEdad='ADULTEZ PRIMARIA').count()
    Ec5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__rangoEdad='ADULTEZ INTERMEDIA').count()
    Ec6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__rangoEdad='ADULTEZ TARDIA').count()
    Ec7 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__rangoEdad='ADULTO MAYOR').count()
    EJ1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__rangoEdad='ADOLECENTE').count()
    EJ2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__rangoEdad='JOVEN').count()
    EJ3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__rangoEdad='ADULTO JOVEN').count()
    EJ4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__rangoEdad='ADULTEZ PRIMARIA').count()
    EJ5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__rangoEdad='ADULTEZ INTERMEDIA').count()
    EJ6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__rangoEdad='ADULTEZ TARDIA').count()
    EJ7 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__rangoEdad='ADULTO MAYOR').count()
    EA1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__rangoEdad='ADOLECENTE').count()
    EA2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__rangoEdad='JOVEN').count()
    EA3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__rangoEdad='ADULTO JOVEN').count()
    EA4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__rangoEdad='ADULTEZ PRIMARIA').count()
    EA5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__rangoEdad='ADULTEZ INTERMEDIA').count()
    EA6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__rangoEdad='ADULTEZ TARDIA').count()
    EA7 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__rangoEdad='ADULTO MAYOR').count()
    EAS1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__rangoEdad='ADOLECENTE').count()
    EAS2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__rangoEdad='JOVEN').count()
    EAS3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__rangoEdad='ADULTO JOVEN').count()
    EAS4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__rangoEdad='ADULTEZ PRIMARIA').count()
    EAS5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__rangoEdad='ADULTEZ INTERMEDIA').count()
    EAS6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__rangoEdad='ADULTEZ TARDIA').count()
    EAS7 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__rangoEdad='ADULTO MAYOR').count()

    Gcl1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__persona__Genero='FEMENINO').count()
    Gcl2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').filter(adoptante__persona__Genero='MASCULINO').count()
    Gc1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__persona__Genero='FEMENINO').count()
    Gc2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').filter(adoptante__persona__Genero='MASCULINO').count()
    GJ1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__persona__Genero='FEMENINO').count()
    GJ2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').filter(adoptante__persona__Genero='MASCULINO').count()
    GA1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__persona__Genero='FEMENINO').count()
    GA2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').filter(adoptante__persona__Genero='MASCULINO').count()
    GAS1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__persona__Genero='FEMENINO').count()
    GAS2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').filter(adoptante__persona__Genero='MASCULINO').count()

    Tp1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='PEQUEÑO').filter(adoptante__tipo_vivienda='CASA PROPIA').count()
    Tp2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='PEQUEÑO').filter(adoptante__tipo_vivienda='CASA ALQUILER').count()
    Tp3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='PEQUEÑO').filter(adoptante__tipo_vivienda='DEPARTAMENTO PROPIO').count()
    Tp4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='PEQUEÑO').filter(adoptante__tipo_vivienda='DEPARTAMENTO ALQUILADO').count()
    Tp5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='PEQUEÑO').filter(adoptante__tipo_vivienda='GARZONIER').count()
    Tp6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='PEQUEÑO').filter(adoptante__tipo_vivienda='OTRO').count()
    Tm1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='MEDIANO').filter(adoptante__tipo_vivienda='CASA PROPIA').count()
    Tm2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='MEDIANO').filter(adoptante__tipo_vivienda='CASA ALQUILER').count()
    Tm3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='MEDIANO').filter(adoptante__tipo_vivienda='DEPARTAMENTO PROPIO').count()
    Tm4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='MEDIANO').filter(adoptante__tipo_vivienda='DEPARTAMENTO ALQUILADO').count()
    Tm5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='MEDIANO').filter(adoptante__tipo_vivienda='GARZONIER').count()
    Tm6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='MEDIANO').filter(adoptante__tipo_vivienda='OTRO').count()
    Tg1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='GRANDE').filter(adoptante__tipo_vivienda='CASA PROPIA').count()
    Tg2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='GRANDE').filter(adoptante__tipo_vivienda='CASA ALQUILER').count()
    Tg3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='GRANDE').filter(adoptante__tipo_vivienda='DEPARTAMENTO PROPIO').count()
    Tg4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='GRANDE').filter(adoptante__tipo_vivienda='DEPARTAMENTO ALQUILADO').count()
    Tg5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='GRANDE').filter(adoptante__tipo_vivienda='GARZONIER').count()
    Tg6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='GRANDE').filter(adoptante__tipo_vivienda='OTRO').count()
    TgG1 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='GIGANTE').filter(adoptante__tipo_vivienda='CASA PROPIA').count()
    TgG2 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='GIGANTE').filter(adoptante__tipo_vivienda='CASA ALQUILER').count()
    TgG3 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='GIGANTE').filter(adoptante__tipo_vivienda='DEPARTAMENTO PROPIO').count()
    TgG4 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='GIGANTE').filter(adoptante__tipo_vivienda='DEPARTAMENTO ALQUILADO').count()
    TgG5 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='GIGANTE').filter(adoptante__tipo_vivienda='GARZONIER').count()
    TgG6 = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        animal__tamano='GIGANTE').filter(adoptante__tipo_vivienda='OTRO').count()

    return render(request, 'Reportes/Organizacion/detalles/Adop.html',
                  {
                      'nav': 'Caninos',
                      'entity_anterior_url': reverse_lazy('rep:reportesOrganizacion:IndiceRepOrg'),
                      'entity_anterior': 'Lista de Reportes',
                      'entity': 'Reporte acerca de la  Especie Canina (Perros)',
                      'titulo': 'Reporte acerca de la  Especie Canina (Perros)',
                      'tituloprincipal': 'Informacion General de los animales Adoptados',
                      'tituloUno': 'Cantidad Registrada de animales adoptados segun  Rando de edad del animal',
                      'tedad1': tedad1, 'tedad2': tedad2, 'tedad3': tedad3, 'tedad4': tedad4, 'tedad5': tedad5,
                      'tituloDos': 'Cantidad Registrada de animales adoptados esterilizados/Castrados, en Gestacion y lactancia segun Genero',
                      'tEsF': tEsF, 'tEsM': tEsM, 'tGF': tGF, 'tLF': tLF,
                      'tituloTres': 'Cantidad Registrada de animales adoptados segun rango de edad del animal y Tipo de vivienda del adoptante',
                      'Vcl1': Vcl1, 'Vcl2': Vcl2, 'Vcl3': Vcl3, 'Vcl4': Vcl4, 'Vcl5': Vcl5, 'Vcl6': Vcl6,
                      'Vc1': Vc1, 'Vc2': Vc2, 'Vc3': Vc3, 'Vc4': Vc4, 'Vc5': Vc5, 'Vc6': Vc6,
                      'Vj1': Vj1, 'Vj2': Vj2, 'Vj3': Vj3, 'Vj4': Vj4, 'Vj5': Vj5, 'Vj6': Vj6,
                      'VA1': VA1, 'VA2': VA2, 'VA3': VA3, 'VA4': VA4, 'VA5': VA5, 'VA6': VA6,
                      'VAS1': VAS1, 'VAS2': VAS2, 'VAS3': VAS3, 'VAS4': VAS4, 'VAS5': VAS5, 'VAS6': VAS6,
                      'tituloCuatro': 'Cantidad Registrada de animales adoptados segun rango de edad del animal y rango de edad del adoptante',
                      'Ecl1': Ecl1, 'Ecl2': Ecl2, 'Ecl3': Ecl3, 'Ecl4': Ecl4, 'Ecl5': Ecl5, 'Ecl6': Ecl6, 'Ecl7': Ecl7,
                      'Ec1': Ec1, 'Ec2': Ec2, 'Ec3': Ec3, 'Ec4': Ec4, 'Ec5': Ec5, 'Ec6': Ec6, 'Ec7': Ec7,
                      'EJ1': EJ1, 'EJ2': EJ2, 'EJ3': EJ3, 'EJ4': EJ4, 'EJ5': EJ5, 'EJ6': EJ6, 'EJ7': EJ7,
                      'EA1': EA1, 'EA2': EA2, 'EA3': EA3, 'EA4': EA4, 'EA5': EA5, 'EA6': EA6, 'EA7': EA7,
                      'EAS1': EAS1, 'EAS2': EAS2, 'EAS3': EAS3, 'EAS4': EAS4, 'EAS5': EAS5, 'EAS6': EAS6, 'EAS7': EAS7,
                      'tituloCinco': 'Cantidad Registrada de animales adoptados segun rango de edad del animal y genero del adoptante',
                      'Gcl1': Gcl1, 'Gcl2': Gcl2, 'Gc1': Gc1, 'Gc2': Gc2, 'GJ1': GJ1, 'GJ2': GJ2, 'GA1': GA1,
                      'GA2': GA2, 'GAS1': GAS1, 'GAS2': GAS2,
                      'tituloSeis': 'Cantidad Registrada de animales adoptados segun rango de tamaño del animal y Tipo de vivienda del adoptante',
                      'Tp1': Tp1, 'Tp2': Tp2, 'Tp3': Tp3, 'Tp4': Tp4, 'Tp5': Tp5, 'Tp6': Tp6,
                      'Tm1': Tm1, 'Tm2': Tm2, 'Tm3': Tm3, 'Tm4': Tm4, 'Tm5': Tm5, 'Tm6': Tm6,
                      'Tg1': Tg1, 'Tg2': Tg2, 'Tg3': Tg3, 'Tg4': Tg4, 'Tg5': Tg5, 'Tg6': Tg6,
                      'TgG1': TgG1, 'TgG2': TgG2, 'TgG3': TgG3, 'TgG4': TgG4, 'TgG5': TgG5, 'TgG6': TgG6,
                  })


def CANrepEnSanAnimOrg(request):
    nOrg = request.user.voluntario_perfil.organizacion.nomorganizacion

    tedad1 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO LACTANTE').count()
    tedad2 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='CACHORRO').count()
    tedad3 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='JOVEN').count()
    tedad4 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO').count()
    tedad5 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        edad_Anim='ADULTO SENIOR').count()

    DisCL1 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='NINGUNO').filter(edad_Anim='CACHORRO LACTANTE').count()
    DisC1 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='NINGUNO').filter(edad_Anim='CACHORRO').count()
    DisJ1 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='NINGUNO').filter(edad_Anim='JOVEN').count()
    DisA1 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='NINGUNO').filter(edad_Anim='ADULTO').count()
    DisAS1 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='NINGUNO').filter(edad_Anim='ADULTO SENIOR').count()
    DisCL2 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='FISICA').filter(edad_Anim='CACHORRO LACTANTE').count()
    DisC2 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='FISICA').filter(edad_Anim='CACHORRO').count()
    DisJ2 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='FISICA').filter(edad_Anim='JOVEN').count()
    DisA2 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='FISICA').filter(edad_Anim='ADULTO').count()
    DisAS2 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='FISICA').filter(edad_Anim='ADULTO SENIOR').count()
    DisCL3 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='AUDITIVA').filter(edad_Anim='CACHORRO LACTANTE').count()
    DisC3 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='AUDITIVA').filter(edad_Anim='CACHORRO').count()
    DisJ3 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='AUDITIVA').filter(edad_Anim='JOVEN').count()
    DisA3 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='AUDITIVA').filter(edad_Anim='ADULTO').count()
    DisAS3 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='AUDITIVA').filter(edad_Anim='ADULTO SENIOR').count()
    DisCL4 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='VISUAL').filter(edad_Anim='CACHORRO LACTANTE').count()
    DisC4 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='VISUAL').filter(edad_Anim='CACHORRO').count()
    DisJ4 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='VISUAL').filter(edad_Anim='JOVEN').count()
    DisA4 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='VISUAL').filter(edad_Anim='ADULTO').count()
    DisAS4 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='VISUAL').filter(edad_Anim='ADULTO SENIOR').count()
    DisCL5 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='OLFATIVA').filter(edad_Anim='CACHORRO LACTANTE').count()
    DisC5 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='OLFATIVA').filter(edad_Anim='CACHORRO').count()
    DisJ5 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='OLFATIVA').filter(edad_Anim='JOVEN').count()
    DisA5 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='OLFATIVA').filter(edad_Anim='ADULTO').count()
    DisAS5 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='OLFATIVA').filter(edad_Anim='ADULTO SENIOR').count()
    DisCL6 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='VOCAL').filter(edad_Anim='CACHORRO LACTANTE').count()
    DisC6 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='VOCAL').filter(edad_Anim='CACHORRO').count()
    DisJ6 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='VOCAL').filter(edad_Anim='JOVEN').count()
    DisA6 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='VOCAL').filter(edad_Anim='ADULTO').count()
    DisAS6 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='VOCAL').filter(edad_Anim='ADULTO SENIOR').count()
    DisCL7 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='MULTIPLE').filter(edad_Anim='CACHORRO LACTANTE').count()
    DisC7 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='MULTIPLE').filter(edad_Anim='CACHORRO').count()
    DisJ7 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='MULTIPLE').filter(edad_Anim='JOVEN').count()
    DisA7 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='MULTIPLE').filter(edad_Anim='ADULTO').count()
    DisAS7 = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=nOrg).filter(
        animal__especie__especies='CANINA').filter(
        datosMedicos__Tipodiscapacidad='MULTIPLE').filter(edad_Anim='ADULTO SENIOR').count()

    return render(request, 'Reportes/Organizacion/detalles/EnSant.html',
                  {
                      'nav': 'Caninos',
                      'entity_anterior_url': reverse_lazy('rep:reportesOrganizacion:IndiceRepOrg'),
                      'entity_anterior': 'Lista de Reportes',
                      'entity': 'Reporte acerca de la  Especie Canina (Perros)',
                      'titulo': 'Reporte acerca de la  Especie Canina (Perros)',
                      'tituloprincipal': 'Informacion General de los animales en Santuarios o Refugios de manera permanente',
                      'tituloUno': 'Cantidad Registrada segun  Rando de edad del animal',
                      'tedad1': tedad1, 'tedad2': tedad2, 'tedad3': tedad3, 'tedad4': tedad4, 'tedad5': tedad5,
                      'tituloDos': 'Cantidad Registrada segun Tipo de discapacidad y rango de edad',
                      'DisCL1': DisCL1, 'DisC1': DisC1, 'DisJ1': DisJ1, 'DisA1': DisA1, 'DisAS1': DisAS1,
                      'DisCL2': DisCL2, 'DisC2': DisC2, 'DisJ2': DisJ2, 'DisA2': DisA2, 'DisAS2': DisAS2,
                      'DisCL3': DisCL3, 'DisC3': DisC3, 'DisJ3': DisJ3, 'DisA3': DisA3, 'DisAS3': DisAS3,
                      'DisCL4': DisCL4, 'DisC4': DisC4, 'DisJ4': DisJ4, 'DisA4': DisA4, 'DisAS4': DisAS4,
                      'DisCL5': DisCL5, 'DisC5': DisC5, 'DisJ5': DisJ5, 'DisA5': DisA5, 'DisAS5': DisAS5,
                      'DisCL6': DisCL6, 'DisC6': DisC6, 'DisJ6': DisJ6, 'DisA6': DisA6, 'DisAS6': DisAS6,
                      'DisCL7': DisCL7, 'DisC7': DisC7, 'DisJ7': DisJ7, 'DisA7': DisA7, 'DisAS7': DisAS7,
                  })
