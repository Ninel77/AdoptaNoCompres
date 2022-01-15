from datetime import datetime, date

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from organizacion.models import (AnimalesDatosB, AnimalesRescatados, AnimalesEnAdopcion,
                                 AnimalesAdoptados, InfoEvaluacion, DocumentosAdopcion,
                                 Adoptante, AnimalesSantuario)

from usuario.models import DatosPersonales

from organizacion.forms import (AnimRescatados, DatoBasicosAnimales, DatosMedicos, AnimEnAdopcion,
                                AnimalesAdop, DatosAdoptante, DocAdopcion, DatosAdoptanteAct, AnimalSantuario)

from usuario.UsuarioSuper.forms import RegPersona
from organizacion.upload import age, rangoEdadAnimal, rangoEdadPersona

from MotorEmparejamiento.models import Dataset


def detalleAnimalC(request, slug):
    print("Ver Detalles")
    animal = None
    animalResc = None
    animalEnAdop = None
    animalAdop = None
    animalSant = None
    evalM = None
    error = None
    message = None
    message1 = None
    message2 = None
    message3 = None
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
                    if AnimalesSantuario.objects.filter(slug=slug).exists():
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
                      'animalSant': animalSant,
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


class ListaAnimalesTodo(ListView):
    model = AnimalesDatosB
    template_name = 'animales/listas/ListaAnimales.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Animales de compañia Registrados'
        organizacionn = self.request.user.voluntario_perfil.organizacion.nomorganizacion
        print("organizacion", organizacionn)
        context['object_list'] = AnimalesDatosB.objects.filter(organizacion__nomorganizacion=organizacionn)
        context['entity'] = 'Lista de los Animales de compañia Registrados'
        context['entity_url'] = reverse_lazy('animales:ListaAnimTodo')

        return context


class ListaAnimalesRehab(ListView):
    model = AnimalesRescatados
    template_name = 'animales/listas/ListaAnimalesEnRehab.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Animales de compañia Ingresados en Rehabilitacion/Observación'
        organizacionn = self.request.user.voluntario_perfil.organizacion.nomorganizacion
        print("organizacion", organizacionn)
        context['object_list'] = AnimalesRescatados.objects.filter(animal__organizacion__nomorganizacion=organizacionn,
                                                                   animal__estado='REHABILITACION')
        context['entity'] = 'Listado de Animales de compañia Ingresados en Rehabilitacion/Observación'
        context['entity_url'] = reverse_lazy('animal:ListaAnimEnRehab')
        context['entity_registro'] = reverse_lazy('animal:RegAnimResc')
        context['entity_registro_nom'] = 'Registrar Nuevo Animal'
        return context


class ListaAnimalesEnAdop(ListView):
    model = AnimalesEnAdopcion
    template_name = 'animales/listas/ListaAnimalesEnAdop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Animales En Adopcion'
        organizacionn = self.request.user.voluntario_perfil.organizacion.nomorganizacion
        print("organizacion", organizacionn)
        context['object_list'] = AnimalesEnAdopcion.objects.filter(animal__organizacion__nomorganizacion=organizacionn,
                                                                   animal__estado='EN ADOPCION')
        context['entity'] = 'Lista de los Animales En Adopcion'
        context['entity_url'] = reverse_lazy('animal:ListaAnimEnAdop')

        return context


class ListaAnimalesAdop(ListView):
    model = AnimalesAdoptados
    template_name = 'animales/listas/ListaAnimalesAdop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Animales Adoptados'
        organizacionn = self.request.user.voluntario_perfil.organizacion.nomorganizacion
        print("organizacion", organizacionn)
        context['object_list'] = AnimalesAdoptados.objects.filter(animal__organizacion__nomorganizacion=organizacionn,
                                                                  animal__estado='ADOPTADO')
        context['entity'] = 'Lista de los Animales Adoptados'
        context['entity_url'] = reverse_lazy('animal:ListaAnimAdop')

        return context


class ListaAnimalesSantuario(ListView):
    model = AnimalesSantuario
    template_name = 'animales/listas/ListaAnimalesSantuario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Animales En Santuarios o refugios de manera permanente'
        organizacionn = self.request.user.voluntario_perfil.organizacion.nomorganizacion
        print("organizacion", organizacionn)
        context['object_list'] = AnimalesSantuario.objects.filter(animal__organizacion__nomorganizacion=organizacionn,
                                                                  animal__estado='EN SANTUARIO')
        context['entity'] = 'Listado de Animales En Santuarios o refugios de manera permanente'
        context['entity_url'] = reverse_lazy('animal:ListaAnimEnSant')

        return context


class ListaAdoptante(ListView):
    model = Adoptante
    template_name = 'animales/listas/ListaAdoptantes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Adoptantes'
        organizacionn = self.request.user.voluntario_perfil.organizacion.nomorganizacion
        print("organizacion", organizacionn)
        context['object_list'] = Adoptante.objects.filter(
            perfil_adoptante__animal__organizacion__nomorganizacion=organizacionn)
        context['entity'] = 'Lista de los Adoptantes de la organizacion'
        context['entity_url'] = reverse_lazy('animal:ListaAdoptantes')

        return context


class RegistroAnimalesRescatados(CreateView):
    model = AnimalesRescatados
    template_name = 'animales/RegistroAnimalesRescatados.html'
    form_class = AnimRescatados
    primer_form_class = DatoBasicosAnimales
    segundo_form_class = DatosMedicos
    success_url = reverse_lazy('animal:ListaAnimEnRehab')

    def get_context_data(self, **kwargs):
        context = super(RegistroAnimalesRescatados, self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form1' not in context:
            context['form1'] = self.primer_form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.segundo_form_class(self.request.GET)
        context['titulo'] = 'Registro Animales Rescatados/Rehabilitacion'
        context['entity'] = 'Registro Animales'
        context['tituloPrim'] = 'Registro Datos Basicos'
        context['tituloTer'] = 'Registro Evaluacion Basica'
        context['tituloSec'] = 'Registro acerca del Ingreso'
        context['accion'] = 'Registrar'
        context['accion2'] = 'Cancelar'
        context['accion2_url'] = reverse_lazy('animal:ListaAnimEnRehab')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form1 = self.primer_form_class(request.POST, request.FILES)
        form2 = self.segundo_form_class(request.POST, request.FILES)
        form3 = form2
        volAcar = self.request.user.voluntario_perfil
        organ = self.request.user.voluntario_perfil.organizacion
        print("Formularios validados", volAcar)
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            animalesResc = form.save(commit=False)
            animalesResc.voluntarioAcargo = volAcar
            datosBaAnim = form1.save(commit=False)
            datosBaAnim.organizacion = organ
            datosBaAnim.situacion = 'VIVO'
            datosBaAnim.save()
            animalesResc.animal = datosBaAnim
            evalMed = form2.save(commit=False)
            evalMed.slug = datosBaAnim.slug
            disc = form2.cleaned_data['discapacidad']
            if disc == False:
                evalMed.Tipodiscapacidad = 'NINGUNO'
            evalMed.save()
            animalesResc.datosMedicos = evalMed
            evalMed2 = InfoEvaluacion.objects.create()
            eval2 = form2.save(commit=False)
            eval2.id = evalMed2.id
            eval2.slug = datosBaAnim.slug
            if disc == False:
                eval2.Tipodiscapacidad = 'NINGUNO'
            eval2.save()
            animalesResc.datosMedicos2 = eval2
            mesesEdad = form.cleaned_data['edadMeses']
            anosEdad = form.cleaned_data['edadAnos']
            rangEdadAnim = rangoEdadAnimal(mesesEdad, anosEdad)
            animalesResc.edad_Anim = rangEdadAnim
            animalesResc.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form1=form1, form2=form2))


def PonerEnAdop(request, slug):
    datosAnim = AnimalesDatosB.objects.get(slug=slug)
    DatAnimalRes = AnimalesRescatados.objects.get(slug=slug)
    infoEvalViejo = InfoEvaluacion.objects.get(id=DatAnimalRes.datosMedicos2_id)
    # infoEvalNuevo = InfoEvaluacion.objects.create()
    # infoEval = InfoEvaluacion.objects.get(id=infoEvalViejo.datosMedicos_id)
    volAcar = request.user.voluntario_perfil
    if request.method == 'GET':

        form = AnimEnAdopcion()
        form1 = DatoBasicosAnimales(instance=datosAnim)
        form2 = DatosMedicos(instance=infoEvalViejo)
    else:
        form = AnimEnAdopcion(request.POST, request.FILES)
        form1 = DatoBasicosAnimales(request.POST, instance=datosAnim)
        form2 = DatosMedicos(request.POST, instance=infoEvalViejo)
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            datosa = form1.save(commit=False)
            datosa.estado = 'EN ADOPCION'
            datosa.save()
            enAdop = form.save(commit=False)
            enAdop.animal = datosa
            enAdop.voluntarioAcargo = volAcar
            evalMed2 = InfoEvaluacion.objects.create()
            eval2 = form2.save(commit=False)
            eval2.id = evalMed2.id
            eval2.slug = datosa.slug
            eval2.save()
            enAdop.datosMedicos = eval2
            mesesEdad = form.cleaned_data['edadMeses']
            anosEdad = form.cleaned_data['edadAnos']
            rangoEdadAnim = rangoEdadAnimal(mesesEdad, anosEdad)
            enAdop.edad_Anim = rangoEdadAnim
            enAdop.save()
            return redirect('animal:ListaAnimEnAdop')

    return render(request, 'animales/RegistroAnimalesEnAdopcion.html',
                  {
                      'form': form,
                      'form1': form1,
                      'form2': form2,
                      'form3': DatAnimalRes,
                      'mensajeEdad': True,
                      'accion': 'Registrar',
                      'titulo': datosAnim.nombre,
                      'entity_anterior_url': reverse('animal:detDatAnim(enAdop)', args=[slug]),
                      'entity_anterior': datosAnim.nombre,
                      'entity': 'Poner en adopcion',
                      'tituloPrim': 'Actualizar Informacion Basica',
                      'tituloSec': 'Agregar informacion para poner en adopcion',
                      'tituloTer': 'Actualizar Datos de Evaluacion',
                      'entity_cancelar_url': reverse('animal:PonerEnAdop', args=[slug, ]),
                      'entity_cancelar': 'Cancelar',
                  })


def VerifAdop(request):
    datosPer = None
    bc = None
    estadop = None
    if request.method == 'GET':
        print(request.GET.get('carnet'))
        carnet = request.GET.get('carnet')
        slug = request.GET.get('slug')
        DatosEnAdop = AnimalesEnAdopcion.objects.get(slug=slug)
        if carnet != None:
            if Adoptante.objects.filter(persona__Carnet=carnet).exists():
                mensaje1 = 'Existe el carnet registrado'
                bc = True
                print(bc, 'existe')
                if Adoptante.objects.filter(persona__Carnet=carnet).filter(estado='BUEN ADOPTANTE'):
                    mensaje2 = 'El nro de carnet esta registrado como BUEN ADOPTANTE'
                    datosPer = DatosPersonales.objects.get(Carnet=carnet)
                    estadop = True
                    print(estadop, 'estado')

                else:
                    mensaje2 = 'El nro de carnet esta registrado como MAL ADOPTANTE'
                    estadop = False
                    print(estadop, 'estado')
            else:
                bc = False
                mensaje1 = 'No se encuentra registrado el carnet'

    return render(request, 'animales/detalles/adopcion.html',
                  {
                      'form6': DatosEnAdop,
                      'accion': 'Registrar',
                      'accion3': 'Verificar',
                      'mensaje1': mensaje1,
                      'mensaje2': mensaje2,
                      'datos': datosPer,
                      'bc': bc,
                      'estadop': estadop,
                      'titulo': 'Registrar Adopcion',
                      'entity': 'Registrar Adopcion',
                      'tituloPrim': 'Datos del Animal',
                      'tituloSec': 'Registrar datos del Adoptante y Documentos',
                      'tituloTer': 'Actualizar datos de la evaluacion',
                  })


def dataset(slug):
    DatosBasicosAnimales = AnimalesDatosB.objects.get(slug=slug)
    DatosIngresos = AnimalesRescatados.objects.get(animal=DatosBasicosAnimales.id)
    DatosAdopcion = AnimalesAdoptados.objects.get(animal=DatosIngresos.id)

    anosAnim = DatosAdopcion.edadAnos
    mesAnim = DatosAdopcion.edadMeses
    RanEdadAnim = DatosAdopcion.edad_Anim
    especie = DatosBasicosAnimales.especie.especies
    raza = DatosBasicosAnimales.raza.raza
    tamano = DatosBasicosAnimales.tamano
    sexo = DatosBasicosAnimales.sexo
    color1 = DatosBasicosAnimales.color1.color
    color2 = DatosBasicosAnimales.color2.color
    ester = DatosAdopcion.datosMedicos.esterilizacion
    disc = DatosAdopcion.datosMedicos.Tipodiscapacidad
    f_in = DatosIngresos.Fecha_Rescate
    f_resc = DatosAdopcion.fechaRegistroAdop
    dias =  f_in.day - f_resc.day
    fecha_nac = DatosAdopcion.adoptante.persona.Fecha_Nac
    edadActual = age(fecha_nac)
    RangoEdadAdop = DatosAdopcion.adoptante.rangoEdad
    SexoAdop = DatosAdopcion.adoptante.persona.Genero
    OcupAdop = DatosAdopcion.adoptante.ocupacion
    VivAdop = DatosAdopcion.adoptante.tipo_vivienda

    data = Dataset.objects.create(
        edadAnos=anosAnim,
        edadMeses=mesAnim,
        edad_anim=RanEdadAnim,
        especie_anim=especie,
        raza_anim=raza,
        tamano_anim=tamano,
        sexo_anim=sexo,
        color_prin=color1,
        color_sec=color2,
        esterilizacion=ester,
        Tipodiscapacidad=disc,
        f_rescate=f_in,
        f_adopcion=f_resc,
        diasEnAdop=dias,
        edad_adop=edadActual,
        rangoEdad=RangoEdadAdop,
        sexo_adop=SexoAdop,
        ocupacion=OcupAdop,
        tipo_vivienda_adop=VivAdop,

    )

    return data


def RegAdop(request, slug):
    volAcar = request.user.voluntario_perfil
    DatosEnAdop = AnimalesEnAdopcion.objects.get(slug=slug)
    animal = AnimalesDatosB.objects.get(id=DatosEnAdop.animal_id)
    animaldat = AnimalesDatosB.objects.get(slug=slug)
    datosMedAnt = InfoEvaluacion.objects.get(id=DatosEnAdop.datosMedicos_id)
    tiempo = datetime.today()
    mensaje1 = None
    mensaje2 = None
    datosPer = None
    mensajeEdad = True

    if request.method == 'GET':
        form = AnimalesAdop(request.FILES)
        form1 = DatoBasicosAnimales(instance=animaldat)
        form2 = DatosAdoptante()
        if datosPer == None:
            form3 = RegPersona()
        else:
            form3 = RegPersona(instance=datosPer)
        form4 = DocAdopcion(request.FILES)
        form5 = DatosMedicos(instance=datosMedAnt)
    else:
        form = AnimalesAdop(request.POST, request.FILES)
        form1 = DatoBasicosAnimales(request.POST, instance=animaldat)
        form2 = DatosAdoptante(request.POST)
        form3 = RegPersona(request.POST)
        form4 = DocAdopcion(request.POST, request.FILES)
        form5 = DatosMedicos(request.POST, instance=datosMedAnt)
        if form5.is_valid() and form4.is_valid() and form3.is_valid() and form1.is_valid():
            print('form3,1,5')
            if form.is_valid() and form2.is_valid():
                fecha_nac = form3.cleaned_data['Fecha_Nac']
                edadActual = age(fecha_nac)
                print(edadActual)
                if edadActual < 18:
                    mensajeEdad = False
                    return render(request, 'animales/RegistroAdopcion(Nuevo2).html',
                                  {
                                      'form': form, 'form1': form1, 'form2': form2,
                                      'form3': form3, 'form4': form4, 'form5': form5,
                                      'form6': DatosEnAdop,
                                      'accion': 'Registrar',
                                      'accion3': 'Verificar',
                                      'titulo': 'Registrar Adopcion',
                                      'entity': 'Registrar Adopcion',
                                      'entity_anterior_url': reverse('animal:detDatAnim(Adop)', args=[slug]),
                                      'entity_anterior': animaldat.nombre,
                                      'tituloPrim': 'Datos del Animal',
                                      'tituloSec': 'Registrar datos del Adoptante y Documentos',
                                      'tituloTer': 'Actualizar datos de la evaluacion',
                                      'mensajeEdad': mensajeEdad,
                                      'mensaje': 'El adoptante es menor de edad',
                                      'entity_cancelar_url': reverse('animal:RegistrarAdop', args=[slug, ]),
                                      'entity_cancelar': 'Cancelar',
                                  })
                else:
                    datAnim = form1.save(commit=False)
                    datAnim.estado = 'ADOPTADO'
                    datAnim.save()
                    adopAnim = form.save(commit=False)
                    adopAnim.voluntarioAcargo = volAcar
                    evalMed2 = InfoEvaluacion.objects.create()
                    eval2 = form5.save(commit=False)
                    eval2.id = evalMed2.id
                    eval2.slug = datAnim.slug
                    eval2.save()
                    adopAnim.datosMedicos = eval2
                    docAdop = form4.save(commit=False)
                    docAdop.slug = datAnim.slug
                    print('docAdop.slug', docAdop.slug)
                    croquis = form4.cleaned_data['docCroquis']
                    serBas = form4.cleaned_data['docServicio']
                    car = form4.cleaned_data['docCarnet']
                    comp = form4.cleaned_data['docCompromiso']
                    if croquis:
                        docAdop.croquis = True
                    if serBas:
                        docAdop.servicio_basico = True
                    if car:
                        docAdop.carnet = True
                    if comp:
                        docAdop.compromiso = True
                    docAdop.save()
                    adopAnim.documentos = docAdop
                    adoptantes = form2.save(commit=False)
                    adoptantes.persona = form3.save()
                    rangoEdadAdop = rangoEdadPersona(edadActual)
                    print('rango edad perosna', rangoEdadAdop)
                    adoptantes.rangoEdad = rangoEdadAdop
                    adoptantes.save()
                    adopAnim.adoptante = adoptantes
                    adopAnim.animal = datAnim
                    mesesEdad = form.cleaned_data['edadMeses']
                    anosEdad = form.cleaned_data['edadAnos']
                    edadAnimal = rangoEdadAnimal(mesesEdad, anosEdad)
                    adopAnim.edad_Anim = edadAnimal
                    adopAnim.save()

                    data = dataset(slug)
                    data.save()

                    return redirect('animal:ListaAnimAdop')

    return render(request, 'animales/RegistroAdopcion(Nuevo2).html',
                  {
                      'form': form,
                      'form1': form1,
                      'form2': form2,
                      'form3': form3,
                      'form4': form4,
                      'form5': form5,
                      'form6': DatosEnAdop,
                      'accion': 'Registrar',
                      'accion3': 'Verificar',
                      'mensaje1': mensaje1,
                      'mensaje2': mensaje2,
                      'mensajeEdad': mensajeEdad,
                      'titulo': 'Registrar Adopcion',
                      'entity': 'Registrar Adopcion',
                      'entity_anterior_url': reverse('animal:detDatAnim(Adop)', args=[slug]),
                      'entity_anterior': animaldat.nombre,
                      'tituloPrim': 'Datos del Animal',
                      'tituloSec': 'Registrar datos del Adoptante y Documentos',
                      'tituloTer': 'Actualizar datos de la evaluacion',
                      'entity_cancelar_url': reverse('animal:RegistrarAdop', args=[slug, ]),
                      'entity_cancelar': 'Cancelar',
                  })


def detalleAdoptante(request, id):
    adoptante = Adoptante.objects.get(id=id)
    animales = AnimalesAdoptados.objects.filter(adoptante__persona__Carnet=adoptante.persona.Carnet)
    return render(request, 'animales/PerfilAdoptante.html',
                  {
                      'tituloprincipal': 'Datos del Adoptante',
                      'adoptante': adoptante,
                      'animales': animales,
                      'titulo': adoptante.persona.Nombre + adoptante.persona.Apellido,
                      'entity_anterior_url': reverse_lazy('animal:ListaAdoptantes'),
                      'entity_anterior': 'Lista de Adoptantes',
                      'entity': adoptante.persona.Nombre + adoptante.persona.Apellido,
                  })


def animalSantuario(request, slug):
    animal = None
    ultimoEst = None
    evalMedAnt = None
    volAcar = request.user.voluntario_perfil
    datosAnim = AnimalesDatosB.objects.get(slug=slug)

    if AnimalesEnAdopcion.objects.filter(slug=slug).exists():
        animal = AnimalesEnAdopcion.objects.get(slug=slug)
        evalMedAnt = InfoEvaluacion.objects.get(id=animal.datosMedicos.id)
        ultimoEst = 'EN ADOPCION'
    elif AnimalesRescatados.objects.filter(slug=slug).exists():
        animal = AnimalesRescatados.objects.get(slug=slug)
        evalMedAnt = InfoEvaluacion.objects.get(id=animal.datosMedicos.id)
        ultimoEst = 'REHABILITACION'

    if request.method == 'GET':
        form = AnimalSantuario()
        form1 = DatoBasicosAnimales(instance=datosAnim)
        form2 = DatosMedicos(instance=evalMedAnt)
    else:
        form = AnimalSantuario(request.POST, request.FILES)
        form1 = DatoBasicosAnimales(request.POST, instance=datosAnim)
        form2 = DatosMedicos(request.POST, instance=evalMedAnt)
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            santuario = form.save(commit=False)
            santuario.voluntarioAcargo = volAcar
            datosAnim = form1.save(commit=False)
            datosAnim.estado = 'EN SANTUARIO'
            datosAnim.save()
            santuario.animal = datosAnim
            santuario.slug = datosAnim.slug
            evalMed2 = InfoEvaluacion.objects.create()
            eval2 = form2.save(commit=False)
            eval2.id = evalMed2.id
            eval2.slug = datosAnim.slug
            eval2.save()
            santuario.datosMedicos = eval2
            mesesEdad = form.cleaned_data['edadMeses']
            anosEdad = form.cleaned_data['edadAnos']
            rangoEdadAnim = rangoEdadAnimal(mesesEdad, anosEdad)
            santuario.edad_Anim = rangoEdadAnim
            santuario.save()
            return redirect('animal:ListaAnimEnSant')

    return render(request, 'animales/RegistroAnimalesSantuario.html',
                  {
                      'form': form,
                      'form1': form1,
                      'form2': form2,
                      'form3': animal,
                      'ulimoEst': ultimoEst,
                      'mensajeEdad': True,
                      'accion': 'Registrar',
                      'titulo': 'Registrar permanentemente en un santuario/refugio',
                      'entity': 'Registrar permanentemente en un santuario/refugio',
                      'entity_anterior_url': reverse('animal:detDatAnim(Sant)', args=[slug]),
                      'entity_anterior': datosAnim.nombre,
                      'tituloPrim': 'Actualizar Informacion Basica',
                      'tituloSec': 'Agregar informacion para Registrar permanentemente en un santuario/refugio',
                      'tituloTer': 'Actualizar Datos de Evaluacion'
                  })
