from datetime import datetime, date
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from organizacion.models import (AnimalesDatosB, AnimalesRescatados, AnimalesEnAdopcion,
                                 AnimalesAdoptados, InfoEvaluacion, DocumentosAdopcion,
                                 Adoptante, AnimalesSantuario)

from usuario.models import DatosPersonales

from organizacion.FormActualizacion.forms import DatoBasicosAnimaless, ActAnimRescatados
from organizacion.forms import (AnimRescatados, DatoBasicosAnimales, DatosMedicos, AnimEnAdopcion,
                                AnimalesAdop, DatosAdoptante, DocAdopcion, DatosAdoptanteAct, AnimalSantuario)
from usuario.UsuarioSuper.forms import RegPersona


class ActualizardatosBAnim(UpdateView):
    model = AnimalesDatosB
    template_name = 'animales/actualizar/ActSoloDatosAnimales.html'
    form_class = DatoBasicosAnimaless

    def get_context_data(self, **kwargs):
        context = super(ActualizardatosBAnim, self).get_context_data(**kwargs)
        slug = self.kwargs.get('slug', None)
        formulario = self.model.objects.get(slug=slug)
        if 'form' not in context:
            context['form'] = self.form_class()
        context['slug'] = slug
        context['titulo'] = 'Actualizar Datos Basicos del Animal de Compañia '
        context['entity_anterior_url'] = reverse('animal:detDatAnim(basicos)', args=[slug])
        context['entity_anterior'] = formulario.nombre
        context['entity'] = 'Actualizar Datos Basicos'
        context['accion'] = 'Actualizar'
        context['accion2'] = 'Cancelar'
        context['entity_cancelar'] = reverse('animal:detDatAnim(basicos)', args=[slug])
        context['accion_limpiar'] = reverse('animal:ActDatosAnim', args=[slug])
        context['accionlimpiar'] = 'Limpiar Modificaciones'
        context['col'] = 2

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_AnimBas = kwargs['slug']
        AnimBas = self.model.objects.get(slug=id_AnimBas)
        form = self.form_class(request.POST, request.FILES, instance=AnimBas)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('animal:detDatAnim(basicos)', args=[id_AnimBas]))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ActualizarAnimResc(UpdateView):
    model = AnimalesRescatados
    model_segundo = AnimalesDatosB
    model_tercero = InfoEvaluacion
    template_name = 'animales/actualizar/ActAnimResc.html'
    form_class = ActAnimRescatados
    segundo_form_class = DatoBasicosAnimales
    tercer_form_class = DatosMedicos

    def get_context_data(self, **kwargs):
        context = super(ActualizarAnimResc, self).get_context_data(**kwargs)
        col = 2
        context['col'] = col
        slug = self.kwargs.get('slug', None)
        EnAdop = self.model.objects.get(slug=slug)
        DatosAnim = self.model_segundo.objects.get(id=EnAdop.animal_id)
        EvalMed = self.model_tercero.objects.get(id=EnAdop.datosMedicos2_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        context['slug'] = slug
        context['titulo'] = 'Actualizar Datos del Ingreso'
        context['accion'] = 'Actualizar'
        context['accion2'] = 'Cancelar'
        context['entity_cancelar'] = reverse('animal:detDatAnim(ingreso)', args=[slug])
        context['accionlimpiar'] = 'Limpiar'
        context['accion_limpiar'] = reverse('animal:ActRehab', args=[slug])
        context['tituloPrim'] = 'Actualizar Datos de Ingreso'
        context['entity_anterior_url'] = reverse('animal:detDatAnim(ingreso)', args=[slug])
        context['entity_anterior'] = DatosAnim.nombre
        context['entity'] = 'Actualizar Datos de Ingreso'
        context['enAdop'] = EnAdop

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_AnimalEnAdopcion = kwargs['slug']
        EnAdop = self.model.objects.get(slug=id_AnimalEnAdopcion)
        form = self.form_class(request.POST, request.FILES, instance=EnAdop)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('animal:detDatAnim(ingreso)', args=[id_AnimalEnAdopcion]))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ActualizarEvalRehab(UpdateView):
    model = AnimalesRescatados
    model_segundo = AnimalesDatosB
    model_tercero = InfoEvaluacion
    template_name = 'animales/actualizar/ActualizarEval.html'
    form_class = AnimRescatados
    segundo_form_class = DatoBasicosAnimales
    tercer_form_class = DatosMedicos

    def get_context_data(self, **kwargs):
        context = super(ActualizarEvalRehab, self).get_context_data(**kwargs)
        col = 2
        context['col'] = col
        slug = self.kwargs.get('slug', None)
        EnAdop = self.model.objects.get(slug=slug)
        DatosAnim = self.model_segundo.objects.get(id=EnAdop.animal_id)
        EvalMed = self.model_tercero.objects.get(id=EnAdop.datosMedicos2_id)
        if 'form3' not in context:
            context['form3'] = self.tercer_form_class(instance=EvalMed)
        context['slug'] = slug
        context['titulo'] = 'Actualizar Evaluacion del Animal ingresado'
        context['accion'] = 'Actualizar'
        context['accion2'] = 'Cancelar'
        context['entity_cancelar'] = reverse('animal:detDatAnim(rehab)', args=[slug])
        context['accionlimpiar'] = 'Limpiar'
        context['accion_limpiar'] = reverse('animal:ActEval', args=[slug])
        context['tituloPrim'] = 'Actualizar Evaluacion del Animal ingresado'
        context['entity_anterior_url'] = reverse('animal:detDatAnim(rehab)', args=[slug])
        context['entity_anterior'] = DatosAnim.nombre
        context['entity'] = 'Actualizar Evaluacion del Animal ingresado'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_AnimalEnAdopcion = kwargs['slug']
        EnAdop = self.model.objects.get(slug=id_AnimalEnAdopcion)
        DatosAnim = self.model_segundo.objects.get(id=EnAdop.animal_id)
        EvalMed = self.model_tercero.objects.get(id=EnAdop.datosMedicos2_id)
        form3 = self.tercer_form_class(request.POST, instance=EvalMed)
        if form3.is_valid():
            form3.save()
            return HttpResponseRedirect(reverse('animal:detDatAnim(rehab)', args=[id_AnimalEnAdopcion]))
        else:
            return self.render_to_response(self.get_context_data(form3=form3))


class ActualizarAnimEnAdop(UpdateView):
    model = AnimalesEnAdopcion
    model_segundo = AnimalesDatosB
    model_tercero = InfoEvaluacion
    template_name = 'animales/actualizar/ActAnimEnAdop.html'
    form_class = AnimEnAdopcion
    segundo_form_class = DatoBasicosAnimales
    tercer_form_class = DatosMedicos
    success_url = reverse_lazy('animal:ListaAnimEnAdop')
    mensajeEdad = True

    def get_context_data(self, **kwargs):
        context = super(ActualizarAnimEnAdop, self).get_context_data(**kwargs)

        pk = self.kwargs.get('pk', 0)
        EnAdop = self.model.objects.get(id=pk)
        DatosAnim = self.model_segundo.objects.get(id=EnAdop.animal_id)
        EvalMed = self.model_tercero.objects.get(id=EnAdop.datosMedicos_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form1' not in context:
            context['form1'] = self.segundo_form_class(instance=DatosAnim)
        if 'form2' not in context:
            context['form2'] = self.tercer_form_class(instance=EvalMed)
        context['id'] = pk
        slug = EnAdop.slug
        print('slug', slug)
        context['slug'] = slug
        context['form3'] = AnimalesRescatados.objects.get(slug=slug)
        context['EnAdop'] = EnAdop
        context['titulo'] = 'Actualizar Datos Animal en adopcion'
        context['tituloPrim'] = 'Actualizar Datos Animal en adopcion'
        context['tituloSec'] = 'Actualizar Datos para poner en Adopcion'
        context['tituloTer'] = 'Actualizar Datos Evaluacion'
        context['accion'] = 'Actualizar'
        context['accion2'] = 'Cancelar'
        context['entity_cancelar'] = reverse('animal:detDatAnim(enAdop)', args=[slug])
        context['accionlimpiar'] = 'Limpiar'
        context['accion_limpiar'] = reverse('animal:ActEnAdop', args=[pk])
        context['entity_anterior_url'] = reverse('animal:detDatAnim(enAdop)', args=[slug])
        context['entity_anterior'] = DatosAnim.nombre
        context['entity'] = 'Actualizar Datos de En Adopcion'
        context['mensajeEdad'] = True
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_AnimalEnAdopcion = kwargs['pk']
        EnAdop = self.model.objects.get(id=id_AnimalEnAdopcion)
        DatosAnim = self.model_segundo.objects.get(id=EnAdop.animal_id)
        EvalMed = self.model_tercero.objects.get(id=EnAdop.datosMedicos_id)
        form = self.form_class(request.POST, request.FILES, instance=EnAdop)
        form1 = self.segundo_form_class(request.POST, instance=DatosAnim)
        form2 = self.tercer_form_class(request.POST, instance=EvalMed)
        slug = EnAdop.slug
        print('slug', slug)
        if form.is_valid() and form2.is_valid() and form1.is_valid():
            form2.save()
            form1.save()
            form.save()
            return HttpResponseRedirect(reverse('animal:detDatAnim(enAdop)', args=(slug,)))
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form1=form1))


class ActualizarAdoptante(UpdateView):
    model = Adoptante
    model_segundo = DatosPersonales
    template_name = 'animales/actualizar/ActAdoptante.html'
    form_class = DatosAdoptanteAct
    segundo_form_class = RegPersona
    success_url = reverse_lazy('animal:ListaAdoptantes')

    def get_context_data(self, **kwargs):
        context = super(ActualizarAdoptante, self).get_context_data(**kwargs)

        pk = self.kwargs.get('pk', 0)
        adoptante = self.model.objects.get(id=pk)
        personaOrg = self.model_segundo.objects.get(id=adoptante.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.segundo_form_class(instance=personaOrg)
        context['id'] = pk
        context['titulo'] = 'Actualizar Datos Adoptante'
        context['accion'] = 'Actualizar'
        context['accion2'] = 'Cancelar'
        context['entity_cancelar'] = reverse('animal:detAdoptante', args=[pk])
        context['entity_anterior_url'] = reverse('animal:detAdoptante', args=[pk])
        context['entity_anterior'] = adoptante.persona.nombrecompleto
        context['entity'] = 'Actualizar Datos de En Adopcion'
        context['mensajeEdad'] = True

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_Adoptante = kwargs['pk']
        adoptante = self.model.objects.get(id=id_Adoptante)
        persona = self.model_segundo.objects.get(id=adoptante.persona_id)
        form = self.form_class(request.POST, request.FILES, instance=adoptante)
        form2 = self.segundo_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form2.save()
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class ActualizarRegAdopcion(UpdateView):
    model = AnimalesAdoptados
    model_segundo = AnimalesDatosB
    model_tercero = Adoptante
    model_cuarto = DatosPersonales
    model_quinto = DocumentosAdopcion
    model_sexto = InfoEvaluacion
    template_name = 'animales/actualizar/ActRegistroAdopcion(Nuevo2).html'
    form_class = AnimalesAdop
    segundo_form_class = DatoBasicosAnimales
    tercer_form_class = DatosAdoptante
    cuarto_form_class = RegPersona
    quinto_form_class = DocAdopcion
    sexto_form_class = DatosMedicos
    success_url = reverse_lazy('animal:detDatAnim')
    mensajeEdad = True
    model_aux = AnimalesEnAdopcion

    def get_context_data(self, **kwargs):
        context = super(ActualizarRegAdopcion, self).get_context_data(**kwargs)

        pk = self.kwargs.get('pk', 0)
        Adop = self.model.objects.get(id=pk)
        DatosAnim = self.model_segundo.objects.get(id=Adop.animal_id)
        DatosAdop = self.model_tercero.objects.get(id=Adop.adoptante_id)
        DatosPersonaA = self.model_cuarto.objects.get(id=DatosAdop.persona_id)
        DocAdop = self.model_quinto.objects.get(id=Adop.documentos_id)
        Datosmedicos = self.model_sexto.objects.get(id=Adop.datosMedicos_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form1' not in context:
            context['form1'] = self.segundo_form_class(instance=DatosAnim)
        if 'form2' not in context:
            context['form2'] = self.tercer_form_class(instance=DatosAdop)
        if 'form3' not in context:
            context['form3'] = self.cuarto_form_class(instance=DatosPersonaA)
        if 'form4' not in context:
            context['form4'] = self.quinto_form_class(instance=DocAdop)
        if 'form5' not in context:
            context['form5'] = self.sexto_form_class(instance=Datosmedicos)
        if 'mensajeEdad' not in context:
            context['mensajeEdad'] = self.mensajeEdad

        context['mensaje'] = 'La Persona debe ser mayor de edad'
        context['id'] = pk
        slug = Adop.slug
        print('slug', slug)
        context['slug'] = slug
        if 'form6' not in context:
            context['form6'] = self.model_aux.objects.get(slug=slug)
        context['accion2'] = 'Cancelar'
        context['titulo'] = 'Actualizar Datos Animal Adoptado'
        context['accion'] = 'Actualizar'
        context['tituloPrim'] = 'Actualizar datos del Animal'
        context['tituloSec'] = 'Actualizar datos Evaluacion'
        context['tituloTer'] = 'Registrar datos para la Adopcion'
        context['tituloCuar'] = 'Registrar Datos Basicos del Adoptante'
        context['tituloQuin'] = 'Registrar datos adoptante'
        context['tituloSex'] = 'Registrar Documentos'
        context['Adop'] = Adop
        context['entity_cancelar'] = reverse('animal:detDatAnim(Adop)', args=[slug])
        context['accionlimpiar'] = 'Limpiar'
        context['accion_limpiar'] = reverse('animal:ActAdop', args=[pk])
        context['entity_anterior_url'] = reverse('animal:detDatAnim(Adop)', args=[slug])
        context['entity_anterior'] = DatosAnim.nombre
        context['entity'] = 'Actualizar Datos de Adopcion'
        context['mensajeEdad'] = True
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_AnimalAdopcion = kwargs['pk']
        Adop = self.model.objects.get(id=id_AnimalAdopcion)
        DatosAnim = self.model_segundo.objects.get(id=Adop.animal_id)
        DatosAdop = self.model_tercero.objects.get(id=Adop.adoptante_id)
        DatosPersonaA = self.model_cuarto.objects.get(id=DatosAdop.persona_id)
        DocAdop = self.model_quinto.objects.get(id=Adop.documentos_id)
        Datosmedicos = self.model_sexto.objects.get(id=Adop.datosMedicos_id)
        form = self.form_class(request.POST, request.FILES, instance=Adop)
        form1 = self.segundo_form_class(request.POST, request.FILES, instance=DatosAnim)
        form2 = self.tercer_form_class(request.POST, request.FILES, instance=DatosAdop)
        form3 = self.cuarto_form_class(request.POST, request.FILES, instance=DatosPersonaA)
        form4 = self.quinto_form_class(request.POST, request.FILES, instance=DocAdop)
        form5 = self.sexto_form_class(request.POST, request.FILES, instance=Datosmedicos)
        tiempo = datetime.today()
        slug = Adop.slug
        print('slug', slug)
        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            fecha_nac = form3.cleaned_data['Fecha_Nac']
            if (fecha_nac.year + 18, fecha_nac.month, fecha_nac.day) > (tiempo.year, tiempo.month, tiempo.day):
                mensajeEdad = False
                return self.render_to_response(
                    self.get_context_data(form=form, form1=form1, form2=form2, form3=form3,
                                          mensajeEdad=mensajeEdad))
            else:
                docAdop = form4.save(commit=False)
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
                form5.save()
                form4.save()
                form3.save()
                form3.save()
                form1.save()
                form.save()
                return HttpResponseRedirect(reverse('animal:detDatAnim(Adop)', args=(slug,)))
        else:
            return self.render_to_response(
                self.get_context_data(form=form, form1=form1, form2=form2, form3=form3, form4=form4, form5=form5))


class ActualizarAnimEnSant(UpdateView):
    model = AnimalesSantuario
    model_segundo = AnimalesDatosB
    model_tercero = InfoEvaluacion
    template_name = 'animales/actualizar/ActAnimEnSant.html'
    form_class = AnimalSantuario
    segundo_form_class = DatoBasicosAnimales
    tercer_form_class = DatosMedicos
    success_url = reverse_lazy('animal:ListaAnimEnSant')
    mensajeEdad = True
    animal = None
    ultimoEst = None

    def get_context_data(self, **kwargs):
        context = super(ActualizarAnimEnSant, self).get_context_data(**kwargs)

        pk = self.kwargs.get('pk', 0)
        EnAdop = self.model.objects.get(id=pk)
        DatosAnim = self.model_segundo.objects.get(id=EnAdop.animal_id)
        EvalMed = self.model_tercero.objects.get(id=EnAdop.datosMedicos_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form1' not in context:
            context['form1'] = self.segundo_form_class(instance=DatosAnim)
        if 'form2' not in context:
            context['form2'] = self.tercer_form_class(instance=EvalMed)
        context['id'] = pk
        slug = EnAdop.slug
        print('slug', slug)
        context['slug'] = slug

        if AnimalesEnAdopcion.objects.filter(slug=slug).exists():
            self.animal = AnimalesEnAdopcion.objects.get(slug=slug)
            self.ultimoEst = 'EN ADOPCION'
        elif AnimalesRescatados.objects.filter(slug=slug).exists():
            self.animal = AnimalesRescatados.objects.get(slug=slug)
            self.ultimoEst = 'REHABILITACION'

        context['form3'] = self.animal
        context['ultimoEst'] = self.ultimoEst
        context['EnAdop'] = EnAdop
        context['titulo'] = 'Actualizar Datos Animal en Santuario/Refugio de manera permanente'
        context['tituloPrim'] = 'Actualizar Datos Animal'
        context['tituloSec'] = 'Actualizar Datos Info del santuario/refugio permanente'
        context['tituloTer'] = 'Actualizar Datos Evaluacion'
        context['accion'] = 'Actualizar'
        context['accion2'] = 'Cancelar'
        context['entity_cancelar'] = reverse('animal:detDatAnim(Sant)', args=[slug])
        context['accionlimpiar'] = 'Limpiar'
        context['accion_limpiar'] = reverse('animal:ActEnSant', args=[pk])
        context['entity_anterior_url'] = reverse('animal:detDatAnim(Sant)', args=[slug])
        context['entity_anterior'] = DatosAnim.nombre
        context['entity'] = 'Actualizar Datos del animal en santuario/refugio de forma permanente'
        context['mensajeEdad'] = True
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_AnimalEnAdopcion = kwargs['pk']
        EnAdop = self.model.objects.get(id=id_AnimalEnAdopcion)
        DatosAnim = self.model_segundo.objects.get(id=EnAdop.animal_id)
        EvalMed = self.model_tercero.objects.get(id=EnAdop.datosMedicos_id)
        form = self.form_class(request.POST, request.FILES, instance=EnAdop)
        form1 = self.segundo_form_class(request.POST, instance=DatosAnim)
        form2 = self.tercer_form_class(request.POST, instance=EvalMed)
        slug = EnAdop.slug
        print('slug', slug)
        if form.is_valid() and form2.is_valid() and form1.is_valid():
            form2.save()
            form1.save()
            form.save()
            return HttpResponseRedirect(reverse('animal:detDatAnim(Sant)', args=(slug,)))
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form1=form1))
