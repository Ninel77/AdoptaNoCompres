from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import Registro, LoginForm, CambioPasswordChangeForm
from usuario.models import DatosPersonales, UsuarioReg, User



def registro(request):
    if request.method == 'POST':
        form = Registro(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print("user form type", type(user))
            persona = DatosPersonales.objects.create()
            user.persona = persona
            user.is_userr = True
            user.rol = 'Usuario Registrado'
            user.save()
            if user.is_userr:
                UsuarioReg.objects.create(user=user)
                print("user form type", type(UsuarioReg))
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = Registro()
    return render(request, 'incioRegistro/registro.html', {
        'form': form,
        'titulo': 'Registro de Usuario',
        'entity': 'Registro de usuario'})


def login_page1(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("llamada")
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            print("usuario", user)
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! inicio sesion'
                return redirect('index')
            else:
                message = 'Error al iniciar sesion. Verificar que el correo y la contraseña hayan sido introducidas de la manera correcta'
    return render(request, 'incioRegistro/inicio.html', context={'form': form, 'message': message})


def cierreSesion(request):
    logout(request)
    messages.success(request, 'sesion finalizada exitosamente')
    return redirect('index')

def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data.get('email')
            print("correo", correo)
            password = form.cleaned_data.get('password')
            print("contraseña", password)
            usuario = authenticate(email=correo,password=password)
            print("usuario", usuario)
            if usuario is not None:
                login(request, usuario)
                message = f'Hello {usuario.username}! You have been logged in'
                return redirect('index')
            else:
                message = 'Error al iniciar sesion!'
    return render(request, 'incioRegistro/inicio.html', context={'form': form, 'message': message})

def cambiar_Contrasena(request):
    if request.method == 'POST':
        form = CambioPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CambioPasswordChangeForm(request.user)
    return render(request, 'incioRegistro/cambiarContraseña.html', {
        'form': form
    })