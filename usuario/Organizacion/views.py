from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from datetime import date

from usuario.Organizacion.forms import (DatoPersonales, UsuarioVoluntario, DatosVoluntario)
from usuario.models import (Voluntario, Organizacion, User, DatosPersonales, Organizador)

from organizacion.FormActualizacion.forms import (DatoPersonalesAct, UsuarioVoluntarioAct, DatosVoluntarioAct,
                                                  UsuarioVoluntarioActPerfil)

from usuario.UsuarioSuper.forms import (RegPersona, ActOrganizacionOrg, RegSuperAdmin, ActRegUsuarioOrg,
                                        ActOrganizacion, RegOrganizadorAct)

class ListaVoluntarios(ListView):
    model = Voluntario
    template_name = 'Organizacion/ListaVoluntarios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Voluntarios'
        organizacionn = self.request.user.encargado_perfil.organizacion.nomorganizacion
        print("organizacion", organizacionn)
        context['object_list'] = Voluntario.objects.filter(organizacion__nomorganizacion=organizacionn)
        context['entity'] = 'Lista Voluntarios'
        context['entity_url'] = reverse_lazy('userLog:org:ListVol')
        context['entity_registro'] = reverse_lazy('userLog:org:RegVol')
        context['entity_registro_nom'] = 'Registrar Nuevo Voluntario'

        return context


class RegVol(CreateView):
    model = Voluntario
    template_name = 'Organizacion/RegVoluntario.html'
    form_class = DatosVoluntario
    # primer_form_class = RegOrganizacion
    segundo_form_class = UsuarioVoluntario
    tercer_form_class = DatoPersonales
    success_url = reverse_lazy('userLog:org:ListVol')
    mensajeEdad = True

    def get_context_data(self, **kwargs):
        context = super(RegVol, self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.segundo_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.tercer_form_class(self.request.GET)
        if 'mensajeEdad' not in context:
            context['mensajeEdad'] = self.mensajeEdad

        context['tituloTer'] = 'Registro Datos Usuario Voluntario'
        context['tituloSec'] = 'Registro Datos Personales '
        context['accion'] = 'Registrar'
        context['accion2'] = 'Cancelar'
        context['mensaje'] = 'El voluntario ya se encuentra Registrado en la organizacion u otra organizacion'
        context['titulo'] = 'Registro de Voluntario'
        context['entity'] = 'Registrar Voluntarios'
        context['entity_url'] = reverse_lazy('userLog:org:RegVol')
        context['entity_cancelar'] = reverse_lazy('userLog:org:ListVol')
        context['entity_anterior_url'] = reverse_lazy('userLog:org:ListVol')
        context['entity_anterior'] = 'Lista de Voluntarios'

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        # form1 = self.primer_form_class(request.POST, request.FILES)
        form2 = self.segundo_form_class(request.POST)
        form3 = self.tercer_form_class(request.POST)
        organizacionn = self.request.user.encargado_perfil.organizacion
        if form3.is_valid() and form2.is_valid() and form.is_valid():
            num_carnet = form3.cleaned_data['Carnet']
            if DatosPersonales.objects.filter(Carnet=num_carnet).exists():
                mensajeEdad = False
                return self.render_to_response(
                    self.get_context_data(form=form, form2=form2, form3=form3,
                                          mensajeEdad=mensajeEdad))
            else:
                usuario = form2.save(commit=False)
                print("user form type", type(usuario))
                usuario.persona = form3.save()
                usuario.rol = 'Voluntario'
                usuario.is_voluntario = True
                usuario.password = '{}{}'.format(str(usuario.persona.Carnet), usuario.username[:4])
                print("contraseña", usuario.password)
                usuario.set_password(usuario.password)
                print("contraseña has", usuario.password)
                usuario.save()
                organ = organizacionn
                print("nuevoreg", organ)
                voluntario = form.save(commit=False)
                print("user form type", type(voluntario))
                print("correo", usuario.email)
                voluntario.user = usuario
                voluntario.organizacion = organ
                voluntario.save()
                return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


class ActualizarVoluntario(UpdateView):
    model = Voluntario
    model_segundo = User
    model_tercero = DatosPersonales
    template_name = 'Organizacion/ActVoluntario.html'
    form_class = DatosVoluntarioAct
    segundo_form_class = UsuarioVoluntarioAct
    tercer_form_class = DatoPersonalesAct
    success_url = reverse_lazy('userLog:org:ListVol')

    def get_context_data(self, **kwargs):
        context = super(ActualizarVoluntario, self).get_context_data(**kwargs)

        pk = self.kwargs.get('pk', 0)
        voluntario = self.model.objects.get(id=pk)
        usuarioVol = self.model_segundo.objects.get(id=voluntario.user_id)
        personaVol = self.model_tercero.objects.get(id=usuarioVol.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.segundo_form_class(instance=usuarioVol)
        if 'form3' not in context:
            context['form3'] = self.tercer_form_class(instance=personaVol)
        context['id'] = pk
        context['mensajeEdad'] = True
        context['titulo'] = 'Actualizar Datos Voluntario'
        context['accion'] = 'Actualizar'
        context['entity_cancelar'] = reverse_lazy('userLog:org:ListVol')
        context['accion2'] = 'Cancelar'
        context['entity_anterior_url'] = reverse_lazy('userLog:org:ListVol')
        context['entity_anterior'] = 'Lista de Voluntarios'
        context['entity'] = 'Actualizar Datos del Voluntario'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_Voluntario = kwargs['pk']
        voluntario = self.model.objects.get(id=id_Voluntario)
        usuarioVol = self.model_segundo.objects.get(id=voluntario.user_id)
        persona = self.model_tercero.objects.get(id=usuarioVol.persona_id)
        form = self.form_class(request.POST, request.FILES, instance=voluntario)
        form2 = self.segundo_form_class(request.POST, instance=usuarioVol)
        form3 = self.tercer_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form3.save()
            form2.save()
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

class PerfilActualizarOrganizador(UpdateView):
    model = Organizador
    model_segundo = User
    model_tercero = DatosPersonales
    template_name = 'Perfiles/Organizador.html'
    form_class = RegOrganizadorAct
    segundo_form_class = ActRegUsuarioOrg
    tercer_form_class = RegPersona
    success_url = reverse_lazy('index')
    mensajeEdad = True

    def get_context_data(self, **kwargs):
        context = super(PerfilActualizarOrganizador, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        admin = self.model.objects.get(id=pk)
        usuarioAdmin = self.model_segundo.objects.get(id=admin.user_id)
        personaAdmin = self.model_tercero.objects.get(id=usuarioAdmin.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.segundo_form_class(instance=usuarioAdmin)
        if 'form3' not in context:
            context['form3'] = self.tercer_form_class(instance=personaAdmin)
        context['id'] = pk
        if 'mensajeEdad' not in context:
            context['mensajeEdad'] = self.mensajeEdad
        context['mensaje'] = 'La Persona debe ser mayor de edad'
        context['titulo'] = 'Perfil'
        context['entity'] = 'Perfil'
        context['accion'] = 'Actualizar'
        context['accion2'] = 'Cancelar'

        context['cambioContraseña'] = 'Actualizar contraseña'
        context['cambioContraseña_url'] = reverse_lazy('CambioContraseña')

        context['entity_cancelar'] = reverse_lazy('index')

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_Admin = kwargs['pk']
        admin = self.model.objects.get(id=id_Admin)
        usuarioAdmin = self.model_segundo.objects.get(id=admin.user_id)
        persona = self.model_tercero.objects.get(id=usuarioAdmin.persona_id)
        form = self.form_class(request.POST, request.FILES, instance=admin)
        form2 = self.segundo_form_class(request.POST, instance=usuarioAdmin)
        form3 = self.tercer_form_class(request.POST, instance=persona)
        tiempo = date.today()
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            fecha_nac = form3.cleaned_data['Fecha_Nac']
            if (fecha_nac.year + 18, fecha_nac.month, fecha_nac.day) > (tiempo.year, tiempo.month, tiempo.day):
                mensajeEdad = False
                return self.render_to_response(
                    self.get_context_data(form=form, form2=form2, form3=form3, mensajeEdad=mensajeEdad))
            else:
                form3.save()
                form2.save()
                form.save()
                return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


class ActualizarOrganizacion(UpdateView):
    model = Organizacion
    template_name = 'Perfiles/Organizacion.html'
    form_class = ActOrganizacionOrg
    success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['titulo'] = 'Actualizar Datos Organizacion'
        context['entity'] = 'Actualizar Datos Organizacion'
        context['accion'] = 'Actualizar'
        context['accion2'] = 'Cancelar'
        context['mensajeEdad'] = True
        context['entity_cancelar'] = reverse_lazy('userLog:org:perEncargado', args=[pk])

        organizacion = self.model.objects.get(id=pk)
        context['organizador'] = Organizador.objects.get(organizacion_id=pk)
        return context

class ActualizarPerfilVoluntario(UpdateView):
    model = Voluntario
    model_segundo = User
    model_tercero = DatosPersonales
    template_name = 'Perfiles/Voluntario.html'
    form_class = RegOrganizadorAct
    segundo_form_class = UsuarioVoluntarioActPerfil
    tercer_form_class = RegPersona
    success_url = reverse_lazy('index')
    mensajeEdad = True

    def get_context_data(self, **kwargs):
        context = super(ActualizarPerfilVoluntario, self).get_context_data(**kwargs)

        pk = self.kwargs.get('pk', 0)
        voluntario = self.model.objects.get(id=pk)
        usuarioVol = self.model_segundo.objects.get(id=voluntario.user_id)
        personaVol = self.model_tercero.objects.get(id=usuarioVol.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.segundo_form_class(instance=usuarioVol)
        if 'form3' not in context:
            context['form3'] = self.tercer_form_class(instance=personaVol)
        context['id'] = pk
        context['mensajeEdad'] = True
        context['titulo'] = 'Actualizar Datos Perfil Voluntario'
        context['accion'] = 'Actualizar'
        context['entity_cancelar'] = reverse_lazy('index')
        context['accion2'] = 'Cancelar'
        context['entity'] = 'Actualizar Datos del Perfil del Voluntario'

        context['cambioContraseña'] = 'Actualizar contraseña'
        context['cambioContraseña_url'] = reverse_lazy('CambioContraseña')

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_Voluntario = kwargs['pk']
        voluntario = self.model.objects.get(id=id_Voluntario)
        usuarioVol = self.model_segundo.objects.get(id=voluntario.user_id)
        persona = self.model_tercero.objects.get(id=usuarioVol.persona_id)
        form = self.form_class(request.POST, request.FILES, instance=voluntario)
        form2 = self.segundo_form_class(request.POST, instance=usuarioVol)
        form3 = self.tercer_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form3.save()
            form2.save()
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))