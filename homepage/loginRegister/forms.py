from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from usuario.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'

    email = forms.EmailField(max_length=255, label='Correo',
                             widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su correo'}))
    password = forms.CharField(max_length=255,label='Contraseña',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}))


class Registro(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña'
        }

        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Nombre de Usuario',
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': 'Ingrse un Correo Electronico',
                }
            )
        }

class CambioPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'