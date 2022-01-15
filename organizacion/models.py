import uuid
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.forms import model_to_dict
from django.utils.translation import gettext_lazy as _

from app.settings import MEDIA_URL

from .choices import (sexo, estadoAdoptante, estadoAnimal, TipoTamanos, tipo_vivienda, Tipoedad, edadAnimal,
                      tipoDiscapacidad, edadAnos, edadMeses, tipoIngresos, tipoVacunas, tipoAlimentacion, estVid,
                      rangoEdad, obsMalAdop)

from usuario.models import Organizacion, DatosPersonales, Voluntario
from django.db.models.signals import pre_save
from django.utils.text import slugify

from organizacion.upload import ( fotoIngreso, fotoPaAdopcion, fotoAdopcion, fotoSantuario)
# Create your models here.

class Especie(models.Model):
    especies = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Especie')
        verbose_name_plural = _('Especies')
        db_table = 'Especie'

    def __str__(self):
        return f'{self.especies}'

    def toJSON(self):
        item = model_to_dict(self)
        return item


class Raza(models.Model):
    raza = models.CharField(max_length=255)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, verbose_name='especies')

    def __str__(self):
        return f'{self.raza} {self.especie}'

    class Meta:
        verbose_name = _('raza')
        verbose_name_plural = _('razas')
        db_table = 'Raza'

class Color(models.Model):
    color = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.color}'

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Color')
        db_table = 'Color'


class InfoEvaluacion(models.Model):
    slug = models.SlugField(null=False, blank=False)
    fechaModificacion = models.DateField(auto_now_add=True)
    tipoVacuna = models.CharField(choices=tipoVacunas, max_length=150, default='NINGUNO', blank=True)
    ultimaFechaV = models.DateField(blank=True, null=True)
    vacAntirrabica = models.BooleanField(default=False)
    ultimaFechaReb = models.DateField(blank=True, null=True)
    masInfoVac = models.TextField(default='Ninguna', blank=True)
    desparacitacion = models.BooleanField(default=False)
    ultimaFechaDes = models.DateField(blank=True, null=True)
    masInfoDes = models.TextField(default='Ninguna', blank=True)
    discapacidad = models.BooleanField(default=False)
    Tipodiscapacidad = models.CharField(choices=tipoDiscapacidad, max_length=255, default='NINGUNO', blank=True)
    masInfoDisca = models.TextField(default='Ninguno', blank=True)
    probCAdultosM = models.BooleanField(default=True)
    probCAdultos = models.BooleanField(default=True)
    probCjovenes = models.BooleanField(default=True)
    probCAdol = models.BooleanField(default=True)
    probCNinosMenores = models.BooleanField(default=True)
    probMujeres = models.BooleanField(default=True)
    probHombres = models.BooleanField(default=True)
    probSocialGatos = models.BooleanField(default=True)
    probSocialPerros = models.BooleanField(default=True)
    probSocialOtros = models.BooleanField(default=True)
    masInfoProbSoc = models.TextField(default='Ninguno', blank=True)
    moquillo = models.BooleanField(default=False)
    parvovirus = models.BooleanField(default=False)
    rabia = models.BooleanField(default=False)
    cutaneaos = models.BooleanField(default=False)
    parasitos = models.BooleanField(default=False)
    desnutricion = models.BooleanField(default=False)
    Depresion = models.BooleanField(default=False)
    Ansiedad = models.BooleanField(default=False)
    masInfoEnfer = models.TextField(default='Ninguno', blank=True)
    esterilizacion = models.BooleanField(default=False)
    fechaEster = models.DateField(null=True, blank=True)
    codigoEster = models.CharField(max_length=255, default=0, blank=True)
    gestacion = models.BooleanField(default=False)
    infoGesta = models.TextField(blank=True)
    lactancia = models.BooleanField(default=False)
    infoLac = models.TextField(max_length=255, blank=True)
    tipoAlim = models.CharField(choices=tipoAlimentacion, max_length=255, default='NO SE CONOCE', blank=True)
    descripcionEval = models.TextField(default='Ninguna Observacion', blank=True)

    class Meta:
        verbose_name = _('Informe de Evaluacion')
        verbose_name_plural = _('Informes de Evaluaciones')
        db_table = 'InfoEvaluacion'

    def __str__(self):
        return f'{self.id} - {self.descripcionEval}'

    def toJSON(self):
        item = model_to_dict(self)
        return item


class AnimalesDatosB(models.Model):
    organizacion = models.ForeignKey(Organizacion, related_name='DatOrganizacion', on_delete=models.CASCADE)
    situacion = models.CharField(choices=estVid, max_length=255, default='VIVO')
    estado = models.CharField(choices=estadoAnimal, max_length=255, default='REHABILITACION')
    slug = models.SlugField(null=False, blank=False, unique=True)
    fechaNaci = models.DateField(null=True, blank=True)
    nombre = models.CharField(max_length=255)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, null=False)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE, null=False)
    tamano = models.CharField(max_length=255, choices=TipoTamanos, default='seleccione el tamaño')
    sexo = models.CharField(max_length=255, choices=sexo)
    color1 = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='color1')
    color2 = models.ForeignKey(Color, blank=True, on_delete=models.CASCADE, related_name='color2')
    descripcion = models.TextField(default='Nin', blank=True)

    def __str__(self):
        return f'{self.id} - {self.nombre}-{self.especie.especies}-{self.raza.raza}-{self.organizacion.nomorganizacion} '

    class Meta:
        verbose_name = _('Animal Datos Basicos')
        verbose_name_plural = _('Animales Datos Basicos')
        db_table = 'DatosBasicosAnimales'

    def toJSON(self):
        item = model_to_dict(self)
        item['especie'] = self.especie.toJSON()
        item['raza'] = self.raza.toJSON()
        item['organizacion'] = self.organizacion.toJSON()
        return item

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()

        return super(AnimalesDatosB, self).save(*args, **kwargs)


def set_slug(sender, instance, *args, **kwargs):
    if instance.organizacion.abreviacion and not instance.slug:
        slug = slugify(
            '{}-{}'.format(instance.organizacion.abreviacion, str(uuid.uuid4())[:4])
        )
        instance.slug = slug


pre_save.connect(set_slug, sender=AnimalesDatosB)


class Adoptante(models.Model):
    persona = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    contactoReferencia = models.IntegerField()
    nomContactoRef = models.CharField(max_length=255)
    estado = models.CharField(choices=estadoAdoptante, max_length=255, default='BUEN ADOPTANTE')
    obsMalAdop = models.CharField(max_length=255, choices=obsMalAdop, default='NINGUNO')
    rangoEdad = models.CharField(max_length=255, choices=rangoEdad)
    email = models.EmailField(blank=False)
    ocupacion = models.CharField(max_length=255, blank=True)
    tipo_vivienda = models.CharField(choices=tipo_vivienda, max_length=255)



    class Meta:
        verbose_name = _('Adoptante')
        verbose_name_plural = _('Adoptantes')
        db_table = 'Adoptante'

    def __str__(self):
        return f'{self.id} {self.persona.Nombre} {self.persona.Apellido}'

    def save(self, *args, **kwargs):
        self.ocupacion = (self.ocupacion).upper()
        if self.nomContactoRef:
            self.nomContactoRef = (self.nomContactoRef).upper()

        return super(Adoptante, self).save(*args, **kwargs)

def docAdopcion1(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #return f'{instance.user.voluntario_perfil.organizacion.abreviacion}/Animales/{instance.slug}/documentos' + filename
    #return f'{instance.animal.organizacion.abreviacion}/Animales/{instance.slug}/documentos' + filename
    slugAnimal = instance.slug
    animal = AnimalesDatosB.objects.get(slug=slugAnimal)
    organizacion = animal.organizacion.abreviacion
    return f'{organizacion}/Animales/{instance.slug}/documentos/' + filename

class DocumentosAdopcion(models.Model):
    slug = models.SlugField(null=False, blank=False)
    croquis = models.BooleanField(default=False)
    docCroquis = models.FileField(upload_to=docAdopcion1, blank=True)
    servicio_basico = models.BooleanField(default=False)
    docServicio = models.FileField(upload_to=docAdopcion1, blank=True)
    carnet = models.BooleanField(default=False)
    docCarnet = models.FileField(upload_to=docAdopcion1, blank=True)
    compromiso = models.BooleanField(default=False)
    docCompromiso = models.FileField(upload_to=docAdopcion1, blank=True)
    Otrodocumento = models.BooleanField(default=False)
    docOtro = models.FileField(upload_to=docAdopcion1, blank=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Documentos Adopcion')
        verbose_name_plural = _('Documentos de Adopcion')
        db_table = 'DocumentosAdopcion'

    def __str__(self):
        return f'{self.id} '


SCORE_Anos = zip(range(0, 26), range(0, 26))
SCORE_meses = zip(range(0, 12), range(0, 12))


class AnimalesRescatados(models.Model):
    slug = models.SlugField(null=False, blank=False, unique=True)
    voluntarioAcargo = models.ForeignKey(Voluntario, on_delete=models.CASCADE)
    animal = models.OneToOneField(AnimalesDatosB, on_delete=models.CASCADE)
    datosMedicos = models.OneToOneField(InfoEvaluacion, on_delete=models.CASCADE, related_name='datosMedicos')
    datosMedicos2 = models.OneToOneField(InfoEvaluacion, on_delete=models.CASCADE, related_name='datosMedicos2')
    tipoIngreso = models.CharField(choices=tipoIngresos, max_length=100, default='RESCATE')
    edad_Anim = models.CharField(max_length=255, blank=True)
    edadAnos = models.IntegerField(choices=edadAnos, default=0)
    edadMeses = models.IntegerField(choices=edadMeses, default=0)
    Fecha_Rescate = models.DateField(default=datetime.now)
    FechaRegistro = models.DateField(default=datetime.now)
    fotoRescate = models.ImageField(upload_to=fotoIngreso, blank=True)
    descripcionRescate = models.TextField(blank=True)
    #STORAge
    class Meta:
        verbose_name = _('Animal Rescatado')
        verbose_name_plural = _('Animales Rescatados')
        db_table = 'AnimalesRescatados'

    def __str__(self):
        return f'{self.id} {self.animal.nombre}'

    def get_image(self):
        if self.fotoRescate:
            return '{}{}'.format(MEDIA_URL, self.fotoRescate)

    def nombreVol(self):
        return f'{self.voluntarioAcargo.user.persona.Nombre} {self.voluntarioAcargo.user.persona.Apellido}'

    def Edad(self):
        if self.edadAnos == 0:
            return f'{self.edadMeses} Meses'
        else:
            return f'{self.edadAnos} Años y {self.edadMeses} Meses'


def set_slugR(sender, instance, *args, **kwargs):
    if instance.animal.slug and not instance.slug:
        instance.slug = slugify(instance.animal.slug)


pre_save.connect(set_slugR, sender=AnimalesRescatados)


class AnimalesEnAdopcion(models.Model):
    animal = models.OneToOneField(AnimalesDatosB, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, blank=False, unique=True)
    voluntarioAcargo = models.ForeignKey(Voluntario, on_delete=models.CASCADE)
    datosMedicos = models.OneToOneField(InfoEvaluacion, on_delete=models.CASCADE)
    fecha_en_Adopcion = models.DateField(default=datetime.now)
    edad_Anim = models.CharField(max_length=255, choices=edadAnimal)
    edadAnos = models.IntegerField(choices=edadAnos, default=0)
    edadMeses = models.IntegerField(choices=edadMeses, default=0)
    fotoEnAdopcion = models.ImageField(upload_to=fotoPaAdopcion, blank=True)
    desCaracter = models.TextField(blank=True)
    desOrigen = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Animal En Adopcion')
        verbose_name_plural = _('Animales en Adopcion')
        db_table = 'AnimalesEnAdopcion'

    def __str__(self):
        return f'Animal: {self.animal.nombre}'

    def get_image(self):
        if self.fotoEnAdopcion:
            return '{}{}'.format(MEDIA_URL, self.fotoEnAdopcion)

    def Edad(self):
        if self.edadAnos == 0:
            return f'{self.edadMeses} Meses'
        else:
            return f'{self.edadAnos} Años y {self.edadMeses} Meses'


def set_slugEn(sender, instance, *args, **kwargs):
    if instance.animal.slug and not instance.slug:
        instance.slug = slugify(instance.animal.slug)


pre_save.connect(set_slugEn, sender=AnimalesEnAdopcion)


class AnimalesAdoptados(models.Model):
    slug = models.SlugField(null=False, blank=False, unique=True)
    animal = models.OneToOneField(AnimalesDatosB, on_delete=models.CASCADE)
    voluntarioAcargo = models.ForeignKey(Voluntario, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(Adoptante, related_name="perfil_adoptante", on_delete=models.CASCADE)
    documentos = models.OneToOneField(DocumentosAdopcion, on_delete=models.CASCADE)
    datosMedicos = models.OneToOneField(InfoEvaluacion, on_delete=models.CASCADE)
    fechaRegistroAdop = models.DateField(default=datetime.now)
    edad_Anim = models.CharField(max_length=255, choices=edadAnimal)
    edadAnos = models.IntegerField(choices=edadAnos, default=0)
    edadMeses = models.IntegerField(choices=edadMeses, default=0)
    fotoAdopcion = models.ImageField(upload_to=fotoAdopcion, null=True, blank=True)
    descripcionAdop = models.TextField(default='Ingrese una descripcion de la adopcion', blank=True)

    class Meta:
        verbose_name = _('Animal Adoptado')
        verbose_name_plural = _('Animales Adoptados')
        db_table = 'AnimalesAdoptados'

    def __str__(self):
        return f'Animal: {self.animal.nombre}- Adoptante: {self.adoptante.persona.Nombre}, {self.adoptante.persona.Apellido}'

    def get_image(self):
        if self.fotoAdopcion:
            return '{}{}'.format(MEDIA_URL, self.fotoAdopcion)

    def nombreVol(self):
        return f'{self.voluntarioAcargo.user.persona.Nombre} {self.voluntarioAcargo.user.persona.Apellido}'

    def Edad(self):
        if self.edadAnos == 0:
            return f'{self.edadMeses} Meses'
        else:
            return f'{self.edadAnos} Años y {self.edadMeses} Meses'


def set_slugAd(sender, instance, *args, **kwargs):
    if instance.animal.slug and not instance.slug:
        instance.slug = slugify(instance.animal.slug)


pre_save.connect(set_slugAd, sender=AnimalesAdoptados)


class AnimalesSantuario(models.Model):
    slug = models.SlugField(null=False, blank=False, unique=True)
    animal = models.OneToOneField(AnimalesDatosB, on_delete=models.CASCADE)
    voluntarioAcargo = models.ForeignKey(Voluntario, on_delete=models.CASCADE)
    datosMedicos = models.OneToOneField(InfoEvaluacion, on_delete=models.CASCADE)
    fechaIngresoSan = models.DateField()
    edad_Anim = models.CharField(max_length=255, choices=edadAnimal, blank=True)
    edadAnos = models.IntegerField(choices=edadAnos, default=0)
    edadMeses = models.IntegerField(choices=edadMeses, default=0)
    foto = models.ImageField(upload_to=fotoSantuario, null=True, blank=True)
    nombreSantuario = models.CharField(max_length=255)
    direccionSantuario = models.CharField(max_length=255)
    nombreEncSan = models.CharField(max_length=255)
    contactoRef = models.IntegerField()
    descripcionSan = models.TextField(default='Ingrese informacion adicional')

    class Meta:
        verbose_name = _('Animal Santuario')
        verbose_name_plural = _('Animales Santuario')
        db_table = 'AnimalesSantuario'

    def save(self, *args, **kwargs):
        self.nombreSantuario = (self.nombreSantuario).upper()
        self.direccionSantuario = (self.direccionSantuario).upper()
        self.nombreEncSan = (self.nombreEncSan).upper()

        return super(AnimalesSantuario, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.animal.nombre}'

    def get_image(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)

    def nombreVol(self):
        return f'{self.voluntarioAcargo.user.persona.Nombre} {self.voluntarioAcargo.user.persona.Apellido}'

    def Edad(self):
        if self.edadAnos == 0:
            return f'{self.edadMeses} Meses'
        else:
            return f'{self.edadAnos} Años y {self.edadMeses} Meses'


def set_slugSan(sender, instance, *args, **kwargs):
    if instance.animal.slug and not instance.slug:
        instance.slug = slugify(instance.animal.slug)


pre_save.connect(set_slugSan, sender=AnimalesSantuario)
