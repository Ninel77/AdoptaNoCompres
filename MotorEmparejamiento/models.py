from django.db import models

from usuario.models import UsuarioReg, User

from organizacion.choices import *
from MotorEmparejamiento.choices import edad, sexo_persona, edadPersona, tiempo, sexo_Animal

from django.utils.translation import gettext_lazy as _

from django.db.models.signals import pre_save
from django.utils.text import slugify


# Create your models here.

class Form_C_preferencia(models.Model):
    user = models.ForeignKey(UsuarioReg, related_name='Form_CPref', on_delete=models.CASCADE)
    slug = models.SlugField(null=False, blank=False, unique=True)
    edad_per = models.IntegerField(choices=edadPersona)
    sex_per = models.CharField(choices=sexo_persona, max_length=255)
    edad_can = models.CharField(choices=edad, max_length=255)
    tamano_can = models.CharField(choices=TipoTamanos, max_length=255)
    sexo_can = models.CharField(choices=sexo_Animal, max_length=255)
    dispnib_tiempo = models.IntegerField(choices= tiempo)
    ninos_menores = models.BooleanField(default=False)
    otro_can = models.BooleanField(default=False)
    otro_gato = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.slug} {self.user.user.username} {self.user.user.email}'

    class Meta:
        verbose_name = _('Formulario_Con_Preferencias')
        verbose_name_plural = _('Formularios_Con_Preferencias')
        db_table = 'Form_C_Prefer'


def set_slugF_C(sender, instance, *args, **kwargs):
    if instance.user.slug and not instance.slug:
        instance.slug = slugify(instance.user.slug)


pre_save.connect(set_slugF_C, sender=Form_C_preferencia)


class Form_S_preferencia(models.Model):
    user = models.ForeignKey(UsuarioReg, related_name='Form_SPref', on_delete=models.CASCADE)
    slug = models.SlugField(null=False, blank=False, unique=True)
    edad_can = models.CharField(choices=edad, max_length=40)
    tipoVivienda = models.CharField(choices=tipo_vivienda, max_length=255)
    edad_persona = models.IntegerField(choices=edadPersona)
    sexo_persona = models.CharField(max_length=20, choices=sexo_persona)
    disp_tiempo = models.IntegerField(choices=tiempo)
    ninos_menores = models.BooleanField(default=False)
    otro_can = models.BooleanField(default=False)
    otro_gato = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.slug} {self.user.user.username} {self.user.user.email}'

    class Meta:
        verbose_name = _('Formulario_Sin_Preferencias')
        verbose_name_plural = _('Formularios_Sin_Preferencias')
        db_table = 'Form_S_Prefer'


def set_slugF_S(sender, instance, *args, **kwargs):
    if instance.user.slug and not instance.slug:
        instance.slug = slugify(instance.user.slug)


pre_save.connect(set_slugF_S, sender=Form_S_preferencia)


class Dataset(models.Model):
    edadAnos = models.IntegerField(choices=edadAnos)
    edadMeses = models.IntegerField(choices=edadMeses)
    edad_anim = models.CharField(max_length=100, blank=True)
    especie_anim = models.CharField(max_length=100, blank=True)
    raza_anim = models.CharField(max_length=100, blank=True)
    tamano_anim = models.CharField(max_length=100, choices=TipoTamanos)
    sexo_anim = models.CharField(max_length=100, choices=sexo)
    color_prin = models.CharField(max_length=100, blank=True)
    color_sec = models.CharField(max_length=100, blank=True)
    esterilizacion = models.BooleanField(default=False)
    Tipodiscapacidad = models.CharField(max_length=255, choices=tipoDiscapacidad, blank=True)
    f_rescate = models.DateField()
    f_adopcion = models.DateField()
    diasEnAdop = models.IntegerField()
    tipoIngreso = models.CharField(choices=tipoIngresos, max_length=100, default='RESCATE')
    edad_adop = models.IntegerField()
    rangoEdad = models.CharField(max_length=255, choices=rangoEdad)
    sexo_adop = models.CharField(max_length=100, choices=genero, blank=True )
    ocupacion = models.CharField(max_length=255, blank=True)
    tipo_vivienda_adop = models.CharField(max_length=100, choices=tipo_vivienda, blank=True)


    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = _('Dataset')
        verbose_name_plural = _('Datasets')
        db_table = 'Dataset'

