from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from datetime import date
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Create your views here.
from usuario.UsuarioSuper.forms import (RegOrganizacion, RegOrganizador, RegUsuarioOrg, RegPersona,
                                        ActOrganizacion, RegSuperAdmin, ActRegUsuarioOrg)
from usuario.UsuarioSuper.forms import RegOrganizadorAct
from usuario.models import Organizador, Organizacion, DatosPersonales, User, Voluntario, SuperUser


class ListaOrganizadores(ListView):
    model = Organizador
    template_name = 'SuperUser/listaOrganizadores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Encargados de Organizacion'
        context['object_list'] = Organizador.objects.all()
        context['entity'] = 'Lista de Encargados de Organizacion'
        context['entity_url'] = reverse_lazy('userLog:superuser:ListaOrg')
        return context


class ListaOrganizacion(ListView):
    model = Organizacion
    template_name = 'SuperUser/listaOrganizaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Organizaciones'
        context['object_list'] = Organizacion.objects.all()
        context['entity'] = 'Lista de Organizaciones'
        context['entity_url'] = reverse_lazy('userLog:superuser:ListaEnOrg')
        context['entity_registro_nom'] = 'Registrar Organización'
        context['entity_registro'] = reverse_lazy('userLog:superuser:RegiOrg')
        return context


class RegistroOrg(CreateView):
    model = Organizador
    template_name = 'SuperUser/RegOrganizacion.html'
    form_class = RegOrganizador
    primer_form_class = RegOrganizacion
    segundo_form_class = RegUsuarioOrg
    tercer_form_class = RegPersona
    success_url = reverse_lazy('userLog:superuser:ListaOrg')
    mensajeEdad = True

    def get_context_data(self, **kwargs):
        context = super(RegistroOrg, self).get_context_data(**kwargs)
        context['titulo'] = 'Registro Organizacion'
        context['tituloSec'] = 'Registro Datos de la Organizacion'
        context['tituloTer'] = 'Registro Datos del Encargado de la Organizacion'
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form1' not in context:
            context['form1'] = self.primer_form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.segundo_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.tercer_form_class(self.request.GET)
        if 'mensajeEdad' not in context:
            context['mensajeEdad'] = self.mensajeEdad
        context['mensaje'] = 'La Persona debe ser mayor de edad'
        context['entity'] = 'Registro de la organizacion'
        context['entity_url'] = reverse_lazy('userLog:superuser:RegiOrg')
        context['entity_cancelar'] = reverse_lazy('userLog:superuser:RegiOrg')
        context['accion'] = 'Registrar'
        context['accion2'] = 'Limpiar'
        context['entity_anterior'] = 'Lista de Organizaciones'
        context['entity_anterior_url'] = reverse_lazy('userLog:superuser:ListaEnOrg')

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        tiempo = datetime.today()
        form = self.form_class(request.POST, request.FILES)
        form1 = self.primer_form_class(request.POST, request.FILES)
        form2 = self.segundo_form_class(request.POST, request.FILES)
        form3 = self.tercer_form_class(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid():
            fecha_nac = form3.cleaned_data['Fecha_Nac']
            if (fecha_nac.year + 18, fecha_nac.month, fecha_nac.day) > (tiempo.year, tiempo.month, tiempo.day):
                mensajeEdad = False
                return self.render_to_response(
                    self.get_context_data(form=form, form1=form1, form2=form2, form3=form3,
                                          mensajeEdad=mensajeEdad))
            else:

                print("Formularios validados")
                usuario = form2.save(commit=False)
                print("user form type", type(usuario))
                usuario.persona = form3.save()
                print("user persona", usuario.persona)
                print("user persona", usuario.persona.Carnet)
                usuario.rol = 'Organizador'
                usuario.is_organizador = True
                usuario.is_voluntario = True
                usuario.password = '{}{}'.format(str(usuario.persona.Carnet), usuario.username[:4])
                print("contraseña", usuario.password)
                usuario.set_password(usuario.password)
                print("contraseña has", usuario.password)
                usuario.save()
                organizacion = form1.save()
                print('direccion', organizacion.fotografia.path)
                organizador = form.save(commit=False)
                print("correo", usuario.email)
                print("contraseña", usuario.password)
                organizador.user = usuario
                organizador.organizacion = organizacion
                organizador.save()
                Voluntario.objects.create(user=usuario, organizacion=organizacion, fecha_inicio=tiempo)
                return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form, form1=form1, form2=form2, form3=form3))


class ActualizarOrganizacion(UpdateView):
    model = Organizacion
    template_name = 'SuperUser/ActOrganizacion.html'
    form_class = ActOrganizacion
    success_url = reverse_lazy('userLog:superuser:ListaOrg')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Datos Organizacion'
        context['entity'] = 'Actualizar Datos Organizacion'
        context['accion'] = 'Actualizar'
        context['accion2'] = 'Cancelar'
        context['mensajeEdad'] = True
        context['entity_cancelar'] = reverse_lazy('userLog:superuser:ListaOrg')
        context['entity_anterior'] = 'Lista de Organizaciones'
        context['entity_anterior_url'] = reverse_lazy('userLog:superuser:ListaEnOrg')
        pk = self.kwargs.get('pk', 0)
        organizacion = self.model.objects.get(id=pk)
        context['organizador'] = Organizador.objects.get(organizacion_id=pk)
        return context


class ActualizarOrganizador(UpdateView):
    model = Organizador
    model_segundo = User
    model_tercero = DatosPersonales
    template_name = 'SuperUser/ActEncargado.html'
    form_class = RegOrganizador
    segundo_form_class = RegUsuarioOrg
    tercer_form_class = RegPersona
    success_url = reverse_lazy('userLog:superuser:ListaEnOrg')
    mensajeEdad = True

    def get_context_data(self, **kwargs):
        context = super(ActualizarOrganizador, self).get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Datos Organizador'
        context['tituloTer'] = 'Datos'
        context['entity'] = 'Actualizar Datos Organizador'
        context['accion'] = 'Actualizar'
        context['accion2'] = 'Cancelar'
        context['entity_cancelar'] = reverse_lazy('userLog:superuser:ListaEnOrg')
        context['entity_anterior'] = 'Lista de Encargados'
        context['entity_anterior_url'] = reverse_lazy('userLog:superuser:ListaEnOrg')
        pk = self.kwargs.get('pk', 0)
        organizador = self.model.objects.get(id=pk)
        usuarioOrg = self.model_segundo.objects.get(id=organizador.user_id)
        personaOrg = self.model_tercero.objects.get(id=usuarioOrg.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.segundo_form_class(instance=usuarioOrg)
        if 'form3' not in context:
            context['form3'] = self.tercer_form_class(instance=personaOrg)
        context['id'] = pk
        if 'mensajeEdad' not in context:
            context['mensajeEdad'] = self.mensajeEdad
        context['mensaje'] = 'La Persona debe ser mayor de edad'
        context['organizador'] = organizador
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_Organizador = kwargs['pk']
        organizador = self.model.objects.get(id=id_Organizador)
        usuarioOrg = self.model_segundo.objects.get(id=organizador.user_id)
        persona = self.model_tercero.objects.get(id=usuarioOrg.persona_id)
        form = self.form_class(request.POST, request.FILES, instance=organizador)
        form2 = self.segundo_form_class(request.POST, instance=usuarioOrg)
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


class ActualizarSuperOrganizador(UpdateView):
    model = SuperUser
    model_segundo = User
    model_tercero = DatosPersonales
    template_name = 'Perfiles/SuperUsuario.html'
    form_class = RegSuperAdmin
    segundo_form_class = ActRegUsuarioOrg
    tercer_form_class = RegPersona
    success_url = reverse_lazy('index')
    mensajeEdad = True

    def get_context_data(self, **kwargs):
        context = super(ActualizarSuperOrganizador, self).get_context_data(**kwargs)
        context['titulo'] = 'Perfil'
        context['entity'] = 'Perfil'
        context['accion'] = 'Actualizar'
        context['accion2'] = 'Cancelar'

        context['entity_cancelar'] = reverse_lazy('index')

        context['cambioContraseña'] = 'Actualizar contraseña'
        context['cambioContraseña_url'] = reverse_lazy('CambioContraseña')
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
