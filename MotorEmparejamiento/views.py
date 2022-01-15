from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, UpdateView, ListView
from django.shortcuts import redirect

from MotorEmparejamiento.models import Form_C_preferencia, Form_S_preferencia, Dataset
from usuario.models import UsuarioReg

from MotorEmparejamiento.forms import FormularioCP, FormularioSP, ModFormCP
from organizacion.models import AnimalesEnAdopcion

from organizacion.upload import rangoEdadPersona

import pandas as pd


class EncuentraAtuMascota(TemplateView):
    template_name = 'MotorEmparejamiento/InicioMotor2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Encuentra a tu mascota'
        context['entity'] = 'Motor de emparejamiento'
        context['entity_url'] = reverse_lazy('EncuentraAtuMascota')
        return context


class DatasetLista(ListView):
    model = Dataset
    template_name = 'MotorEmparejamiento/ListaDataset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de datos referente a las adopciones'
        context['entity'] = 'Listado de datos referente a las adopciones'
        return context


def InfoAlgoritmo(request):
    if request.user.is_authenticated:
        user = request.user.perfil_usuarioReg.slug
        if Form_C_preferencia.objects.filter(slug=user).exists():
            return render(request, 'MotorEmparejamiento/AlgoritmoEmp/InfoFconPrefExist.html',
                          {
                              'titulo': 'Informacion del funcionamiento del Algoritmo de Recomendacion',
                              'entity': 'Info Algoritmo Recomendacion',
                              'entity_url': reverse_lazy('motor:InfoAlg'),
                          })
        else:
            return render(request, 'MotorEmparejamiento/AlgoritmoEmp/InfoFconPref.html',
                          {
                              'titulo': 'Informacion del funcionamiento del Algoritmo de Recomendacion',
                              'entity': 'Info Algoritmo Recomendacion',
                              'entity_url': reverse_lazy('motor:InfoAlg'),
                          })
    else:
        return render(request, 'MotorEmparejamiento/AlgoritmoEmp/InfoFconPref.html',
                      {
                          'titulo': 'Informacion del funcionamiento del Algoritmo de Recomendacion',
                          'entity': 'Info Algoritmo Recomendacion',
                          'entity_url': reverse_lazy('motor:InfoAlg'),
                      })


def InfoSistema(request):
    if request.user.is_authenticated:
        user = request.user.perfil_usuarioReg.slug
        if Form_S_preferencia.objects.filter(slug=user).exists():
            return render(request, 'MotorEmparejamiento/SistemaEmp/InfoFsinPrefExist.html',
                          {
                              'titulo': 'Informacion del funcionamiento del Sistema de Recomendacion',
                              'entity': 'Info Sistema Recomendacion',
                              'entity_url': reverse_lazy('motor:InfoSis'),
                          })
        else:
            return render(request, 'MotorEmparejamiento/SistemaEmp/InfoFsinPref.html',
                          {
                              'titulo': 'Informacion del funcionamiento del Sistema de Recomendacion',
                              'entity': 'Info Sistema Recomendacion',
                              'entity_url': reverse_lazy('motor:InfoSis'),
                          })
    else:
        return render(request, 'MotorEmparejamiento/SistemaEmp/InfoFsinPref.html',
                      {
                          'titulo': 'Informacion del funcionamiento del Sistema de Recomendacion',
                          'entity': 'Info Sistema Recomendacion',
                          'entity_url': reverse_lazy('motor:InfoSis'),
                      })


@login_required
def createFormCP(request):
    user = request.user.perfil_usuarioReg
    slug = request.user.perfil_usuarioReg.slug
    if request.method == 'GET':
        form = FormularioCP()
    else:
        form = FormularioCP(request.POST)
        if form.is_valid():
            formCP = form.save(commit=False)
            print("Form C pref type", type(formCP))
            formCP.user = user
            formCP.save()
            # return redirect('motor:ResAlgoritmo', args=(slug,))
            return HttpResponseRedirect(reverse('motor:ResAlgoritmo', args=[slug]))

    return render(request, 'MotorEmparejamiento/AlgoritmoEmp/FormConPref.html', {
        'form': form,
        'titulo': 'Registro Datos Formulario de preferencias',
        'entity': 'Registro Datos Formulario de preferencias',
    })


class ActFormCP(UpdateView):
    model = Form_C_preferencia
    template_name = 'MotorEmparejamiento/AlgoritmoEmp/FormConPref.html'
    form_class = FormularioCP

    def get_context_data(self, **kwargs):
        context = super(ActFormCP, self).get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Datos Formulario con Preferencias'
        context['accion'] = 'Actualizar'
        context['entity'] = 'Actualizar formulario'

        slug = self.kwargs.get('slug', None)
        formulario = self.model.objects.get(slug=slug)
        if 'form' not in context:
            context['form'] = self.form_class()
        context['slug'] = slug
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_formCP = kwargs['slug']
        formCP = self.model.objects.get(slug=id_formCP)
        form = self.form_class(request.POST, request.FILES, instance=formCP)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('motor:ResAlgoritmo', args=[id_formCP]))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class AlgEmparejamiento(ListView):
    model = AnimalesEnAdopcion
    template_name = 'MotorEmparejamiento/AlgoritmoEmp/Resultados.html'

    def get_context_data(self, **kwargs):
        context = super(AlgEmparejamiento, self).get_context_data(**kwargs)
        slug = self.kwargs.get('slug', None)

        form = Form_C_preferencia.objects.get(slug=slug)
        edadCan = form.edad_can
        tamanoCan = form.tamano_can
        generoCan = form.sexo_can
        edadPer = form.edad_per
        generoPer = form.sex_per
        dispTiempo = form.dispnib_tiempo
        ninosPeq = form.ninos_menores
        otroCan = form.otro_can
        otroFel = form.otro_gato

        rangEdadPer = rangoEdadPersona(edadPer)

        if edadCan == 'NINGUNO':
            resPrev = AnimalesEnAdopcion.objects.filter(animal__estado='EN ADOPCION').filter(
                animal__especie__especies='CANINA').filter(animal__tamano=tamanoCan)
        else:
            resPrev = AnimalesEnAdopcion.objects.filter(animal__estado='EN ADOPCION').filter(
                animal__especie__especies='CANINA').filter(edad_Anim=edadCan).filter(animal__tamano=tamanoCan)

        if generoCan != 'INDIFERENTE':
            resPrev = resPrev.filter(animal__sexo=generoCan)

        if generoPer == 'FEMENINO':
            resPrev = resPrev.exclude(datosMedicos__probMujeres=False)
        elif generoPer == 'MASCULINO':
            resPrev = resPrev.exclude(datosMedicos__probHombres=False)

        if rangEdadPer == 'ADOLECENTE':
            resPrev = resPrev.exclude(datosMedicos__probCAdol=False)
        elif rangEdadPer == 'JOVEN' or rangEdadPer == 'ADULTO JOVEN':
            resPrev = resPrev.exclude(datosMedicos__probCjovenes=False)
        elif rangEdadPer == 'ADULTEZ PRIMARIA' or rangEdadPer == 'ADULTEZ INTERMEDIA' or rangEdadPer == 'ADULTEZ TARDIA':
            resPrev = resPrev.exclude(datosMedicos__probCjovenes=False)
        elif rangEdadPer == 'ADULTO MAYOR':
            resPrev = resPrev.exclude(datosMedicos__probCjovenes=False)

        resPrev = filtradoFinal(resPrev, otroCan, otroFel, ninosPeq, dispTiempo)

        context['titulo'] = 'Resultado del emparejamiento'

        context['object_list'] = resPrev
        context['entity'] = 'Resultados'
        context['entity_anterior'] = 'Formulario Algoritmo de emparejamiento'
        context['entity_anterior_url'] = reverse_lazy('motor:ActFormCP', args=[slug, ])

        return context


def detAnimAlg(request, slug):
    animalenAdop = AnimalesEnAdopcion.objects.get(slug=slug)
    slug = request.user.perfil_usuarioReg.slug
    return render(request, 'homepage/DetallesAnimales.html',
                  {
                      'animalenAdop': animalenAdop,
                      'titulo': animalenAdop.animal.nombre,
                      'entity': animalenAdop.animal.nombre,
                      'entity_reverse': 'Resultados del emparejamiento',
                      'entity_reverse_url': reverse_lazy('motor:ResAlgoritmo', args=[slug, ]),
                  })


@login_required
def createFormSP(request):
    slug = request.user.perfil_usuarioReg.slug
    if request.method == 'POST':
        form = FormularioSP(request.POST)
        if form.is_valid():
            formSP = form.save(commit=False)
            print("Form C pref type", type(formSP))
            userReg = UsuarioReg.objects.get(user=request.user)
            formSP.user = userReg
            formSP.save()
            # return redirect('motor:InfoSis')
            return HttpResponseRedirect(reverse('motor:ResRecomendacion', args=[slug]))

    else:
        form = FormularioSP()
    return render(request, 'MotorEmparejamiento/SistemaEmp/FormSinPref.html', {
        'form': form,
        'titulo': 'Registro de Datos Formulario Sin Preferencia',
        'entity': 'Registro de Datos Formulario Sin Preferencia'

    })


class ActFormSP(UpdateView):
    model = Form_S_preferencia
    template_name = 'MotorEmparejamiento/SistemaEmp/FormSinPref.html'
    form_class = FormularioSP

    def get_context_data(self, **kwargs):
        context = super(ActFormSP, self).get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Datos Formulario Sin Preferencias'
        context['accion'] = 'Actualizar'
        slug = self.kwargs.get('slug', None)
        formulario = self.model.objects.get(slug=slug)
        if 'form' not in context:
            context['form'] = self.form_class()
        context['slug'] = slug
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_formCP = kwargs['slug']
        formCP = self.model.objects.get(slug=id_formCP)
        form = self.form_class(request.POST, request.FILES, instance=formCP)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('motor:ResRecomendacion', args=[id_formCP]))

        else:
            return self.render_to_response(self.get_context_data(form=form))


class SistemaRecomendacion(ListView):
    model = AnimalesEnAdopcion
    template_name = 'MotorEmparejamiento/SistemaEmp/Resultados.html'

    def get_context_data(self, **kwargs):
        context = super(SistemaRecomendacion, self).get_context_data(**kwargs)
        slug = self.kwargs.get('slug', None)

        datosFormulario = Form_S_preferencia.objects.get(slug=slug)

        especie = 'CANINA'
        edadCan = datosFormulario.edad_can
        edadePersona = datosFormulario.edad_persona
        tipoVivienda = datosFormulario.tipoVivienda
        sexoPersona = datosFormulario.sexo_persona
        dispTiempo = datosFormulario.disp_tiempo
        ninosPeq = datosFormulario.ninos_menores
        otroCan = datosFormulario.otro_can
        otroFel = datosFormulario.otro_gato
        rangoedad = rangoEdadPersona(edadePersona)

        animEnAdop = AnimalesEnAdopcion.objects.filter(animal__estado=especie).filter(animal__estado='EN ADOPCION')

        print('--------------******------------')
        print(rangoedad)
        data = Dataset.objects.all().values()

        dp = pd.DataFrame(data)

        dp = dp.drop(labels=['edadAnos', 'edadMeses', 'color_prin', 'color_sec', 'esterilizacion',
                             'Tipodiscapacidad', 'f_rescate', 'f_adopcion', 'diasEnAdop', 'edad_adop',
                             'tipoIngreso', 'ocupacion'], axis=1)
        print(dp)
        print(dp.columns)
        dataEdadAdop = dp[dp.especie_anim == especie]
        dataEdadAdop = dataEdadAdop[dataEdadAdop.rangoEdad == rangoedad]

        tamanoInfo = dataEdadAdop[dataEdadAdop.tipo_vivienda_adop == tipoVivienda]

        canttamano = tamanoInfo["tamano_anim"].value_counts()

        tamanoUno = tamanoInfo["tamano_anim"].value_counts().index.tolist()[0]

        VarGenInfo = dataEdadAdop[dataEdadAdop.sexo_adop == sexoPersona]
        cantSexAnim = VarGenInfo["sexo_anim"].value_counts()

        sex_Anim = VarGenInfo["sexo_anim"].value_counts().index.tolist()[0]

        cantEdadAnim = VarGenInfo["edad_anim"].value_counts()
        edad_AnimUno = VarGenInfo["edad_anim"].value_counts().index.tolist()[0]

        # RESULTADOS PRINCIPALES

        resPrin = animEnAdop.filter(animal__tamano=tamanoUno).filter(animal__sexo=sex_Anim).filter(
            edad_Anim=edadCan)
        resPrin = filtradoFinal(resPrin, otroCan, otroFel, ninosPeq, dispTiempo)

        resUno = animEnAdop.filter(animal__tamano=tamanoUno).filter(animal__sexo=sex_Anim).filter(
            edad_Anim=edad_AnimUno)
        resUno = filtradoFinal(resUno, otroCan, otroFel, ninosPeq, dispTiempo)

        # Segundo

        cantTam = len(canttamano)

        if cantTam > 1:
            tamanoDos = tamanoInfo["tamano_anim"].value_counts().index.tolist()[1]
            resdOS = animEnAdop.filter(animal__tamano=tamanoDos)
        else:
            tamanoDos = tamanoUno
            resdOS = animEnAdop.filter(animal__tamano=tamanoDos)

        cantGen = len(cantSexAnim)

        if cantGen > 1:
            sex_AnimDos = VarGenInfo["sexo_anim"].value_counts().index.tolist()[1]
            print(sex_AnimDos)
            resdOS = resdOS.filter(animal__sexo=sex_AnimDos)
        else:
            sex_AnimDos = sex_Anim
            resdOS = resdOS.filter(animal__sexo=sex_AnimDos)

        cantedadA = len(cantEdadAnim)

        if cantedadA > 1:
            edad_AnimDos = VarGenInfo["edad_anim"].value_counts().index.tolist()[1]
            print(edad_AnimDos)
            resdOS = resdOS.filter(edad_Anim=edad_AnimDos)
        else:
            edad_AnimDos = edad_AnimUno
            resdOS = resdOS.filter(edad_Anim=edad_AnimDos)

        resdOS = filtradoFinal(resdOS, otroCan, otroFel, ninosPeq, dispTiempo)

        context['titulo'] = 'Resultado del emparejamiento'
        context['form'] = datosFormulario
        context['tituloUno'] = 'Resultados principales'
        context['object_listUno'] = resPrin
        context['tamanoPrin'] = tamanoUno
        context['GeneroPrin'] = sex_Anim
        context['tituloDos'] = 'Resultados alternativos (1)'
        context['object_listDos'] = resUno
        context['edadCanUno'] = edad_AnimUno
        context['RangoEdad'] = rangoedad
        context['tituloTres'] = 'Resultados alternativos (2)'
        context['object_listTres'] = resdOS
        context['tamanoDos'] = tamanoDos
        context['GeneroDos'] = sex_AnimDos
        context['edadCanDos'] = edad_AnimDos

        context['entity'] = 'Resultados'
        context['entity_anterior'] = 'Formulario Sistema de recomendación'
        context['entity_anterior_url'] = reverse_lazy('motor:ActFormSP', args=[slug, ])

        return context


def detAnimRecom(request, slug):
    animalenAdop = AnimalesEnAdopcion.objects.get(slug=slug)
    slug = request.user.perfil_usuarioReg.slug
    return render(request, 'homepage/DetallesAnimales.html',
                  {
                      'animalenAdop': animalenAdop,
                      'titulo': animalenAdop.animal.nombre,
                      'entity': animalenAdop.animal.nombre,
                      'entity_reverse': 'Resultados del emparejamiento',
                      'entity_reverse_url': reverse_lazy('motor:ResRecomendacion', args=[slug, ]),
                  })


def filtradoFinal(resPrev, otroCan, otroFel, ninosPeq, dispTiempo):
    if otroCan == True:
        resPrev = resPrev.exclude(datosMedicos__probSocialPerros=False)
    elif otroFel == True:
        resPrev = resPrev.exclude(datosMedicos__probSocialGatos=False)

    if ninosPeq == True:
        resPrev = resPrev.exclude(datosMedicos__probCNinosMenores=False)

    if dispTiempo < 8:
        resPrev = resPrev.exclude(datosMedicos__Tipodiscapacidad='FISICA')
        resPrev = resPrev.exclude(datosMedicos__Tipodiscapacidad='AUDITIVA')
        resPrev = resPrev.exclude(datosMedicos__Tipodiscapacidad='VISUAL')
        resPrev = resPrev.exclude(datosMedicos__Tipodiscapacidad='OLFATIVA')
        resPrev = resPrev.exclude(datosMedicos__Tipodiscapacidad='VOCAL')
        resPrev = resPrev.exclude(datosMedicos__Tipodiscapacidad='MULTIPLE')

    return resPrev
