from django.forms import *
from django import forms

from usuario.models import DatosPersonales, User, Voluntario
from organizacion.models import AnimalesDatosB
from organizacion.models import (AnimalesRescatados, AnimalesEnAdopcion,
                                 AnimalesAdoptados, Adoptante, DocumentosAdopcion)

class DatoPersonalesAct(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['Nombre'].widget.attrs['readonly'] = 'readonly'
        self.fields['Apellido'].widget.attrs['readonly'] = 'readonly'
        self.fields['Carnet'].widget.attrs['readonly'] = 'readonly'
        self.fields['Extencion'].widget.attrs['readonly'] = 'readonly'
        self.fields['Fecha_Nac'].widget.attrs['readonly'] = 'readonly'
        self.fields['Genero'].widget.attrs['readonly'] = 'readonly'

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

        widgets = {
            'Extencion': TextInput(),
            'Genero': TextInput()
        }


class UsuarioVoluntarioAct(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['readonly'] = 'readonly'
        self.fields['email'].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active']
        # exclude = ['password1', 'password2']
        labels = {
            'username': 'username',
            'email': 'email',
            'is_active': 'Estado',
        }
class UsuarioVoluntarioActPerfil(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['readonly'] = 'readonly'
        self.fields['email'].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = User
        fields = ['username', 'email',]
        # exclude = ['password1', 'password2']
        labels = {
            'username': 'username',
            'email': 'email',
        }


class DatosVoluntarioAct(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['fecha_inicio'].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Voluntario
        fields = ['fecha_inicio']
        labels = {
            'fecha_inicio': 'Fecha Inicio del Voluntariado',
        }


class DatoBasicosAnimaless(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['descripcion'].widget.attrs['style'] = 'height: 100px;'

    class Meta:
        model = AnimalesDatosB
        fields = '__all__'
        exclude = ['organizacion', 'estado', 'slug']
        labels = {
            'situacion': 'Estado',
            'nombre': 'Nombre',
            'especie': 'Especie',
            'raza': 'Raza',
            'tamano': 'Tamaño',
            'sexo': 'Genero',
            'color1': 'Color pelaje dominante',
            'color2': 'Color pelaje secundario',
            'fechaNaci': 'Fecha de Nacimiento',
            'descripcion': 'Informacion adicional respecto a rasgos/ caracteristicas del animal',

        }

class ActAnimRescatados(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['descripcionRescate'].widget.attrs['style'] = 'height: 50px;'

    class Meta:
        model = AnimalesRescatados
        fields = '__all__'
        exclude = ['animal', 'voluntarioAcargo', 'FechaRegistro', 'slug', 'datosMedicos', 'datosMedicos2', 'edad_Anim',
                   'Fecha_Rescate']
        labels = {
            'tipoIngreso': 'Tipo de ingreso',
            'edadAnos': 'Años',
            'edadMeses': 'Meses',
            'fotoRescate': 'Foto del rescate',
            'descripcionRescate': 'Descripcion del rescate del animal de compañia',
        }

