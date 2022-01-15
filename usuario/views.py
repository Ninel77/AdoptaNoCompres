from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponseRedirect

from usuario.models import (User, DatosPersonales, UsuarioReg)
from usuario.UsuarioSuper.forms import (RegPersonaBasico, RegUsuarioAct, ActRegUsuarioOrg)
from django.urls import reverse_lazy

# Create your views here.

class ActualizarPerfilUsuarioRegistrado(UpdateView):
    model = UsuarioReg
    model_segundo = User
    model_tercero = DatosPersonales
    template_name = 'Perfiles/UsuarioRegis.html'
    form_class = RegUsuarioAct
    segundo_form_class = ActRegUsuarioOrg
    tercer_form_class = RegPersonaBasico
    success_url = reverse_lazy('index')
    mensajeEdad = True

    def get_context_data(self, **kwargs):
        context = super(ActualizarPerfilUsuarioRegistrado, self).get_context_data(**kwargs)

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
        context['titulo'] = 'Actualizar Datos Perfil Usuario Registrado'
        context['accion'] = 'Actualizar'
        context['entity_cancelar'] = reverse_lazy('index')
        context['accion2'] = 'Cancelar'
        context['entity'] = 'Actualizar Datos Perfil Usuario Registrado'
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


