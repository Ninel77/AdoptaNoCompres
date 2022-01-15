from django.forms import *
from django import forms

from MotorEmparejamiento.models import Form_C_preferencia, Form_S_preferencia

class FormularioCP(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'
            form.field.widget.attrs['class'] = 'form-control font-weight-bold border border-info'
        #self.fields['ninos_menores'].widget.attrs['class'] = 'form-check-input'
    class Meta:
        model = Form_C_preferencia
        fields = '__all__'
        exclude = ['user', 'slug']
        labels = {
            'edad_can': '¿Que edad desea que tenga el Can?',
            'tamano_can': '¿Que tamaño desea que tenga el Can',
            'sexo_can': '¿Que genero desea que tenga el can',
            'edad_per': 'Ingrese su edad',
            'sex_per': 'Ingrese su Genero',
            'dispnib_tiempo': 'Con cuanto tiempo (en horas) dispone al dia (6:00 a.m - 11:00 p.m)',
            'ninos_menores': '¿Convives con algun niño menor?',
            'otro_can': '¿Convives con al menos un Can (Perro)',
            'otro_gato': '¿Convives con al menos un Felino (Gato)',
        }



class FormularioSP(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Form_S_preferencia
        fields = '__all__'
        exclude = ['user','slug']
        labels = {
            'tipoVivienda':'Escoja su tipo de vivienda:',
            'edad_persona':'Ingrese su edad',
            'sexo_persona':'Ingrese su genero',
            'edad_can':'Ingrese la edad del can que desea',
            'disp_tiempo':'Con cuanto tiempo (horas) dispone al dia (6:00 a.m - 11:00 p.m)',
            'ninos_menores': '¿Convives con algun niño menor?',
            'otro_can': '¿Convives con al menos un Can (Perro)',
            'otro_gato': '¿Convives con al menos un Felino (Gato)',
        }

class ModFormCP(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Form_C_preferencia
        fields = '__all__'
        exclude = ['user', 'slug']
        labels = {
            'edad_can': '¿Que edad desea que tenga el Can?',
            'tamano_can': '¿Que tamaño desea que tenga el Can',
            'sexo_can': '¿Que genero desea que tenga el can',
            'edad_per': 'Ingrese su edad',
            'sex_per': 'Ingrese su Genero',
            'dispnib_tiempo': 'Con cuanto tiempo (en horas) dispone al dia (6:00 a.m - 11:00 p.m)',
            'ninos_menores': '¿Convives con algun niño menor?',
            'otro_can': '¿Convives con al menos un Can (Perro)',
            'otro_gato': '¿Convives con al menos un Felino (Gato)',
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data