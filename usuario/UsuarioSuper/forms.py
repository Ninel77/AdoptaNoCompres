from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from django import forms
from datetime import date

from usuario.models import Organizacion, Organizador, User, DatosPersonales, SuperUser, UsuarioReg


class RegOrganizacion(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nomorganizacion'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['abreviacion'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['departamento'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['ciudad'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['nombreContacto'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['nombreContacto2'].widget.attrs['style'] = 'text-transform:uppercase'

    class Meta:
        model = Organizacion
        fields = '__all__'
        exclude = ['estado']
        labels = {
            'nomorganizacion': 'Nombre de la Organizacion',
            'abreviacion': 'Abreviación',
            'departamento': 'Departamento',
            'ciudad': 'Ciudad',
            'fechaCreacion': 'Fecha de Fundación : (ej. 2017-08-09)',
            'correo': 'Correo de la Organización',
            'facebook': 'Link de la pagina de Facebook',
            'otraRedSocial': 'Link de otra pagina social',
            'whatsapp': 'Numero de contacto principal',
            'nombreContacto': 'Nombre del contacto principal',
            'contacto2': 'Numero de contacto secundario',
            'nombreContacto2': 'Nombre del contacto secundario',
            'fotografia': 'Imagen del Logo de la organizacion',
            'descripcion': 'Ingrese una Descripcion de la organizacion (Mision, Vision, Objetivos, entre otros)'
        }


class RegOrganizador(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'


    class Meta:
        model = Organizador
        fields = '__all__'
        exclude = ['user', 'slug', 'organizacion']
        labels = {
            'avatar': 'Fotografia de perfil (Opcional)'
        }


class RegUsuarioOrg(ModelForm):
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
            'username': 'Nombre de usuario',
            'email': 'Correo electronico'
        }


class RegPersona(ModelForm):
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
        self.fields['Edif'].widget.attrs['style'] = 'text-transform:uppercase'

    class Meta:
        model = DatosPersonales
        fields = '__all__'
        labels = {
            'Nombre': 'Nombre(s)',
            'Apellido': 'Apellido(s)',
            'Carnet': 'Nro de Carnet',
            'Extencion': 'Extencion',
            'Genero': 'Sexo',
            'Fecha_Nac': 'Fecha de Nacimiento',
            'Celular': 'Numero de celular',
            'Departamento': 'Departamento',
            'Ciudad': 'Ciudad',
            'Dir_zona': 'Zona',
            'Dir_calleOt': 'Direccion',
            'Dir_num': 'Numero de vivienda o de edificio',
            'Edif': 'Nombre del edificio',
            'Dep': 'Nro de departamento',
        }

class ActOrganizacion(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
            form.field.widget.attrs['readonly'] = 'readonly'
        self.fields['estado'].widget.attrs['readonly'] = False
        self.fields['fotografia'].widget.attrs['class'] = 'card card-img-top'


    class Meta:
        model = Organizacion
        fields = '__all__'
        labels = {
            'estado': 'Estado de la organizacion (activo/Inactivo)',
            'nomorganizacion': 'Nombre de la Organizacion',
            'abreviacion': 'Abreviación',
            'departamento': 'Departamento',
            'ciudad': 'Ciudad',
            'fechaCreacion': 'Fecha de Fundación : (ej. 2017-08-09)',
            'correo': 'Correo de la Organización',
            'facebook': 'Link de la pagina de Facebook',
            'otraRedSocial': 'Link de otra pagina social',
            'whatsapp': 'Numero de contacto principal',
            'nombreContacto': 'Nombre del contacto principal',
            'contacto2': 'Numero de contacto secundario',
            'nombreContacto2': 'Nombre del contacto secundario',
            'fotografia': 'Imagen del Logo de la organizacion',
            'descripcion': 'Ingrese una Descripcion de la organizacion (Mision, Vision, Objetivos, entre otros)'
        }

class RegOrganizadorAct(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['avatar'].widget.attrs['readonly'] = 'readonly'
    class Meta:
        model = Organizador
        fields = '__all__'
        exclude = ['user', 'slug', 'organizacion']
        labels = {
            'avatar': 'Fotografia de perfil (Opcional)'
        }

class RegSuperAdmin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'


    class Meta:
        model = SuperUser
        fields = '__all__'
        exclude = ['user', 'slug']
        labels = {
            'avatar': 'Fotografia de perfil (Opcional)'
        }

class ActRegUsuarioOrg(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
            form.field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = User
        fields = ['username', 'email']
        # exclude = ['password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electronico'
        }

class ActOrganizacionOrg(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['fotografia'].widget.attrs['class'] = 'card card-img-top'
        self.fields['departamento'].widget.attrs['readonly'] = 'readonly'
        self.fields['ciudad'].widget.attrs['readonly'] = 'readonly'
        self.fields['fechaCreacion'].widget.attrs['readonly'] = 'readonly'
        self.fields['nomorganizacion'].widget.attrs['readonly'] = 'readonly'


    class Meta:
        model = Organizacion
        fields = '__all__'
        exclude = ['estado']
        labels = {
            'estado': 'Estado de la organizacion (activo/Inactivo)',
            'nomorganizacion': 'Nombre de la Organizacion',
            'abreviacion': 'Abreviación',
            'departamento': 'Departamento',
            'ciudad': 'Ciudad',
            'fechaCreacion': 'Fecha de Fundación : (ej. 2017-08-09)',
            'correo': 'Correo de la Organización',
            'facebook': 'Link de la pagina de Facebook',
            'otraRedSocial': 'Link de otra pagina social',
            'whatsapp': 'Numero de contacto principal',
            'nombreContacto': 'Nombre del contacto principal',
            'contacto2': 'Numero de contacto secundario',
            'nombreContacto2': 'Nombre del contacto secundario',
            'fotografia': 'Imagen del Logo de la organizacion',
            'descripcion': 'Ingrese una Descripcion de la organizacion (Mision, Vision, Objetivos, entre otros)'
        }

        widgets = {
            'departamento': TextInput()

        }

class RegUsuarioAct(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['avatar'].widget.attrs['readonly'] = 'readonly'
    class Meta:
        model = UsuarioReg
        fields = '__all__'
        exclude = ['user', 'slug', 'organizacion']
        labels = {
            'avatar': 'Fotografia de perfil (Opcional)'
        }
class RegPersonaBasico(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['Nombre'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['Apellido'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['Departamento'].widget.attrs['style'] = 'text-transform:uppercase'

    class Meta:
        model = DatosPersonales
        fields = '__all__'
        exclude = ['Carnet','Extencion','Fecha_Nac', 'Ciudad', 'Dir_zona', 'Dir_calleOt', 'Dir_num', 'Edif', 'Dep']
        labels = {
            'Nombre': 'Nombre(s)',
            'Apellido': 'Apellido(s)',
            'Genero': 'Sexo',
            'Celular': 'Numero de celular',
            'Departamento': 'Departamento',
        }