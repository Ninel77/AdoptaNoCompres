from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from django import forms

from usuario.models import DatosPersonales, User, Voluntario


class DatoPersonales(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['Nombre'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['Apellido'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['Departamento'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['Ciudad'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['Dir_zona'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['Dir_calleOt'].widget.attrs['style'] = 'text-transform:uppercase'

    class Meta:
        model = DatosPersonales
        fields = '__all__'
        labels = {
            'Nombre': 'Nombre(s)',
            'Apellido': 'Apellidos',
            'Carnet': 'Nro de Carnet',
            'Extencion': 'Extencion',
            'Genero': 'Sexo',
            'Fecha_Nac': 'Fecha de Nacimiento',
            'Celular': 'Numero de celular',
            'Departamento': 'Departamento',
            'Ciudad': 'Ciudad',
            'Dir_zona': 'Zona',
            'Dir_calleOt': 'Direccion',
            'Dir_num': 'Numero de vivienda o edificio',
            'Edif': 'Nombre del Edificio',
            'Dep': 'Numero de Departamento',
        }


class UsuarioVoluntario(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = User
        fields = ['username', 'email']
        # exclude = ['password1', 'password2']
        labels = {
            'username': 'username',
            'email': 'email'
        }


class DatosVoluntario(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Voluntario
        fields = ['fecha_inicio', 'avatar']
        labels = {
            'fecha_inicio': 'Fecha Inicio del Voluntariado',
            'avatar': 'Fotografia de perfil (Opcional)'
        }
