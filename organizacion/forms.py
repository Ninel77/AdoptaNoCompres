from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from django import forms

from organizacion.models import AnimalesDatosB, InfoEvaluacion
from organizacion.models import (AnimalesRescatados, AnimalesEnAdopcion,
                                 AnimalesAdoptados, Adoptante, DocumentosAdopcion,
                                 AnimalesSantuario)


class DatoBasicosAnimales(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['style'] = 'text-transform:uppercase'

    class Meta:
        model = AnimalesDatosB
        fields = '__all__'
        exclude = ['organizacion', 'estado', 'slug', 'situacion']
        labels = {
            'nombre': 'Nombre',
            'especie': 'Especie',
            'raza': 'Raza',
            'tamano': 'Tamaño',
            'sexo': 'Genero',
            'color1': 'Color pelaje dominante',
            'color2': 'Color pelaje secundario',
            'fechaNaci': 'Fecha de Nacimiento (2020-08-07)',
            'descripcion': 'Informacion adicional respecto a rasgos/ caracteristicas del animal',
        }


class DatosMedicos(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-check font-weight-bold border border-info'
        self.fields['tipoVacuna'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['ultimaFechaV'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['ultimaFechaReb'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['masInfoVac'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['masInfoVac'].widget.attrs['style'] = 'height: 50px;'
        self.fields['masInfoVac'].widget.attrs['autocomplete'] = 'off'
        self.fields['ultimaFechaDes'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['masInfoDes'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['masInfoDes'].widget.attrs['style'] = 'height: 50px;'
        self.fields['masInfoDes'].widget.attrs['autocomplete'] = 'off'
        self.fields['Tipodiscapacidad'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['masInfoDisca'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['masInfoDisca'].widget.attrs['style'] = 'height: 50px;'
        self.fields['masInfoDisca'].widget.attrs['autocomplete'] = 'off'
        self.fields['masInfoProbSoc'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['masInfoProbSoc'].widget.attrs['style'] = 'height: 50px;'
        self.fields['masInfoProbSoc'].widget.attrs['autocomplete'] = 'off'
        self.fields['masInfoEnfer'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['masInfoEnfer'].widget.attrs['style'] = 'height: 50px;'
        self.fields['masInfoEnfer'].widget.attrs['autocomplete'] = 'off'
        self.fields['fechaEster'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['codigoEster'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['infoGesta'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['infoGesta'].widget.attrs['style'] = 'height: 50px;'
        self.fields['infoGesta'].widget.attrs['autocomplete'] = 'off'
        self.fields['infoLac'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['infoLac'].widget.attrs['style'] = 'height: 50px;'
        self.fields['infoLac'].widget.attrs['autocomplete'] = 'off'
        self.fields['tipoAlim'].widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
        self.fields['descripcionEval'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['descripcionEval'].widget.attrs['style'] = 'height: 50px;'
        self.fields['descripcionEval'].widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = InfoEvaluacion
        fields = '__all__'
        exclude = ['fechaModificacion', 'slug']
        labels = {
            'tipoVacuna': 'Tipo de Vacuna',
            'ultimaFechaV': 'Fecha de la vacunacion',
            'vacAntirrabica': 'Vac. Antirrabica',
            'ultimaFechaReb': 'Ultima fecha de la vacuna antirrabica',
            'masInfoVac': 'Informacion adicional respecto a las vacunas',
            'desparacitacion': 'Desparacitacion',
            'ultimaFechaDes': 'Ultima fecha de Desparacitacion',
            'masInfoDes': 'Informacion adicional respecto a la desparacitacion',
            'discapacidad': 'Discapacidad',
            'Tipodiscapacidad': 'Tipo',
            'masInfoDisca': 'Informacion adicional respecto alguna discapacidad',
            'masInfoProbSoc': 'Informacion adicional respecto a los problemas de socializacion',
            'masInfoEnfer': 'Informacion adicional de alguna enfermedad(es)',
            'esterilizacion': 'Esterilizacion/Castracion',
            'fechaEster': 'Fecha ',
            'codigoEster': 'Codigo',
            'gestacion': 'En Gestacion (Esta preñada/embarazada)',
            'infoGesta': 'Informacion adicional del estado de Gestacion',
            'lactancia': 'Dando de lactar/amamantar (Con Crias)',
            'infoLac': 'Informacion adicional del estado de Lactancia',
            'tipoAlim': 'Tipo de Alimentacion',
            'descripcionEval': 'Informacion adicional de la evaluacion',

        }


class AnimRescatados(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['descripcionRescate'].widget.attrs['style'] = 'height: 50px;'

    class Meta:
        model = AnimalesRescatados
        fields = '__all__'
        exclude = ['animal', 'voluntarioAcargo', 'FechaRegistro', 'slug', 'datosMedicos', 'datosMedicos2', 'edad_Anim']
        labels = {
            'tipoIngreso': 'Tipo de ingreso',
            'edadAnos': 'Años',
            'edadMeses': 'Meses',
            'Fecha_Rescate ': 'Fecha de Rescate',
            'fotoRescate': 'Foto del rescate',
            'descripcionRescate': 'Descripcion del rescate del animal de compañia',
        }


class AnimEnAdopcion(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['desCaracter'].widget.attrs['style'] = 'height: 50px;'
        self.fields['desOrigen'].widget.attrs['style'] = 'height: 50px;'

    class Meta:
        model = AnimalesEnAdopcion
        fields = '__all__'
        exclude = ['animal', 'voluntarioAcargo', 'edad_Anim', 'fecha_en_Adopcion', 'slug', 'datosMedicos']
        labels = {
            'edadAnos': 'Años',
            'edadMeses': 'Meses',
            'fotoEnAdopcion': 'Foto del animal en adopcion',
            'desCaracter': 'Descripcion adicional de las caracteristicas fisicas, comportamiento, caracter u otro del animal',
            'desOrigen': 'Descripcion adicional del origen del animal dentro de la organizacion',
        }


class AnimalesAdop(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['descripcionAdop'].widget.attrs['style'] = 'height: 50px;'

    class Meta:
        model = AnimalesAdoptados
        fields = ['edadAnos', 'edadMeses', 'fotoAdopcion', 'descripcionAdop']
        exclude = ['fechaRegistroAdop', 'datosMedicos', 'slug', 'edad_Anim', 'animal', 'voluntarioAcargo',
                   'adoptante', 'documentos']
        labels = {
            'edadAnos': 'Años',
            'edadMeses': 'Meses',
            'fotoAdopcion': 'Foto del animal Adoptado',
            'descripcionAdop': 'Descripcion adicional de la adopcion del animal',
        }


class DatosAdoptante(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['ocupacion'].widget.attrs['style'] = 'text-transform:uppercase'

    class Meta:
        model = Adoptante
        fields = '__all__'
        exclude = ['persona', 'estado', 'rangoEdad', 'obsMalAdop']
        labels = {
            'email': 'Correo',
            'ocupacion': 'Ocupacion',
            'tipo_vivienda': 'Tipo de vivienda',
            'contactoReferencia': 'Contacto de referencia',
            'nomContactoRef': 'Nombre del contacto de referencia',
        }


class DatosAdoptanteAct(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Adoptante
        fields = '__all__'
        exclude = ['persona', 'rangoEdad']
        labels = {
            'estado': 'Estado',
            'email': 'Correo',
            'ocupacion': 'Ocupacion',
            'tipo_vivienda': 'Tipo de vivienda',
            'contactoReferencia': 'Contacto de referencia',
            'nomContactoRef': 'Nombre del contacto de referencia',
            'obsMalAdop': 'Razones por las cuales es Mal Adoptante',
        }


class DocAdopcion(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-check'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = DocumentosAdopcion
        fields = '__all__'
        exclude = ['croquis', 'servicio_basico', 'carnet', 'compromiso', 'slug']
        labels = {
            'croquis': '¿Se tiene el croquis?',
            'docCroquis': 'Documento del croquis',
            'servicio_basico': '¿Se tiene la fotocopia de algun servicio basico?',
            'docServicio': 'Fotocopia del servicio Basico (agua, Luz, gas)',
            'carnet': '¿Se tiene la fotocopia de carnet?',
            'docCarnet': 'Fotocopia de carnet',
            'compromiso': '¿Se tiene el documento de compromiso?',
            'docCompromiso': 'Documento del compromiso',
            'descripcion': 'Observacion(es)',

        }

class AnimalSantuario(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm font-weight-bold border border-info'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombreSantuario'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['direccionSantuario'].widget.attrs['style'] = 'text-transform:uppercase'
        self.fields['nombreEncSan'].widget.attrs['style'] = 'text-transform:uppercase'

    class Meta:
        model = AnimalesSantuario
        fields = '__all__'
        exclude = ['slug', 'animal', 'voluntarioAcargo', 'datosMedicos']
        labels = {
            'fechaIngresoSan' : 'Fecha de ingreso al santuario',
            'edadAnos' : 'Años',
            'edadMeses' : 'Meses',
            'foto' : 'Fotografia del ingreso al santuario',
            'nombreSantuario' : 'Nombre del santuario',
            'direccionSantuario' : 'Direccion del santuario',
            'nombreEncSan' : 'Nombre del encargado del santuario',
            'descripcionSan' : 'descripcion del ingreso al santuario',
            'contactoRef' : 'Contacto de referencia del santuario',
        }