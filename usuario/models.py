import uuid
from django.db import models
from django.conf import settings
from django.forms import model_to_dict

from app.settings import MEDIA_URL, STATIC_URL

from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from django.utils.text import slugify

from .choices import rol, Ext, estado, genero

from usuario.upload import (fotoSuperUsuario, logoOrganizacion, fotoVoluntarios, fotoUsuarioReg)


# Create your models here.


class DatosPersonales(models.Model):
    Nombre = models.CharField(max_length=255, default='Usuario')
    Apellido = models.CharField(max_length=255, default='Invitado')
    Carnet = models.IntegerField(default=00000000)
    Extencion = models.CharField(max_length=255, choices=Ext, default='ninguno')
    Genero = models.CharField(choices=genero, max_length=20, default='NoDefinido')
    Fecha_Nac = models.DateField(default='2021-01-01')
    Telefono = models.IntegerField(null=True, blank=True)
    Celular = models.IntegerField(default=00000000)
    Departamento = models.CharField(max_length=255, default='LA PAZ', choices=Ext)
    Ciudad = models.CharField(max_length=255, default='vacio')
    Dir_zona = models.CharField(max_length=255, default='vacio')
    Dir_calleOt = models.CharField(max_length=255, default='vacio')
    Dir_num = models.IntegerField(default=00)
    Edif = models.CharField(max_length=100, blank=True, null=True)
    Dep = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.Nombre = (self.Nombre).upper()
        self.Apellido = (self.Apellido).upper()
        self.Departamento = (self.Departamento).upper()
        self.Ciudad = (self.Ciudad).upper()
        self.Dir_zona = (self.Dir_zona).upper()
        self.Dir_calleOt = (self.Dir_calleOt).upper()
        if self.Edif:
            self.Edif = (self.Edif).upper()

        return super(DatosPersonales, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} {self.Nombre} {self.Apellido} {self.Carnet}'

    class Meta:
        verbose_name = _('Persona')
        verbose_name_plural = _('Personas')
        db_table = 'DatosPersonales'

    def nombrecompleto(self):
        return f'{self.Nombre} {self.Apellido}'

    def direccionCompletaCasa(self):
        return f'{self.Departamento}, {self.Ciudad}, Zona {self.Dir_zona}, {self.Dir_calleOt}, Nro {self.Dir_num}'

    def direccionCompletadepartamento(self):
        return f'{self.Departamento}, {self.Ciudad}, Zona {self.Dir_zona}, {self.Dir_calleOt}, ' \
               f'Nro {self.Dir_num}, Nombre edificio {self.Edif}, Nro Departamento {self.Dep}'


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        values = [email, username]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))

        for field_usuario, value in field_value_map.items():
            if not value:
                raise ValueError('Se debe establecer {}'.format(field_usuario))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        persona = DatosPersonales.objects.create()
        extra_fields.setdefault('persona', persona)
        extra_fields.setdefault('rol', 'SuperUsuario')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return SuperUser.objects.create(user=self._create_user(email, username, password, **extra_fields))


class User(AbstractBaseUser, PermissionsMixin):
    persona = models.OneToOneField(DatosPersonales, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(_('Usuario'), max_length=255, unique=True)
    email = models.EmailField(_('correo'), blank=False, unique=True)
    rol = models.CharField(_('Roles'), max_length=255, choices=rol)
    fecha_reg = models.DateField(_('Fecha Registro'), auto_now_add=True)
    is_staff = models.BooleanField(_('Estado Staff'), default=False)
    is_active = models.BooleanField(_('Activo'), default=True)
    is_superuser = models.BooleanField(_('Estado superusuario'), default=False)
    is_organizador = models.BooleanField(_('Estado Organizador'), default=False)
    is_voluntario = models.BooleanField(_('Estado voluntario'), default=False)
    is_userr = models.BooleanField(_('Estado usuario registrado'), default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email} - {self.username}'

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
        db_table = 'User'

    def get_full_usuario(self):
        return self.username

    def get_short_usuario(self):
        return self.username.split()[0]


class SuperUser(models.Model):
    user = models.OneToOneField(User, related_name="SuperUser_perfil", on_delete=models.CASCADE)
    slug = models.SlugField(null=False, blank=False, unique=True)
    avatar = models.ImageField(upload_to=fotoSuperUsuario, null=True, blank=True, default='img/Admi.png')

    def __str__(self):
        return f' {self.user.persona.Nombre}-{self.user.persona.Apellido}-{self.user.rol}'

    class Meta:
        verbose_name = _('SuperUser')
        verbose_name_plural = _('SuperUsers')
        db_table = 'SuperUser'

    def get_image(self):
        if self.avatar:
            return '{}{}'.format(MEDIA_URL, self.avatar)
        else:
            return '{}{}'.format(STATIC_URL, 'img/Admi.png')


def set_SuperAdmi(sender, instance, *args, **kwargs):
    if instance.user.is_superuser and not instance.slug:
        slug = slugify(
            '{}-{}'.format(instance.user.rol, str(uuid.uuid4())[:4])
        )

        instance.slug = slug


pre_save.connect(set_SuperAdmi, sender=SuperUser)


def fotoLogo(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    abreviacion = instance.abreviacion
    return f'{abreviacion}/logo/' + filename


class Organizacion(models.Model):
    nomorganizacion = models.CharField(_('Nombre Organizacion'), max_length=255, unique=True)
    abreviacion = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=150, choices=Ext)
    ciudad = models.CharField(max_length=150)
    fechaCreacion = models.DateField()
    correo = models.EmailField()
    facebook = models.URLField()
    otraRedSocial = models.URLField(blank=True)
    whatsapp = models.IntegerField()
    nombreContacto = models.CharField(max_length=255)
    contacto2 = models.IntegerField()
    nombreContacto2 = models.CharField(max_length=255, null=True)
    fotografia = models.ImageField(upload_to=fotoLogo, null=False, blank=False)
    descripcion = models.TextField()
    estado = models.CharField(choices=estado, max_length=25, default='Activo')

    def __str__(self):
        return f'{self.nomorganizacion}-({self.abreviacion})'

    def save(self, *args, **kwargs):
        self.nomorganizacion = (self.nomorganizacion).upper()
        self.departamento = (self.departamento).upper()
        self.ciudad = (self.ciudad).upper()
        self.nombreContacto = (self.nombreContacto).upper()
        self.nombreContacto2 = (self.nombreContacto2).upper()
        if self.abreviacion:
            self.abreviacion = (self.abreviacion).upper()

        return super(Organizacion, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Organizacion')
        verbose_name_plural = _('Organizaciones')
        db_table = 'Organizacion'

    def getimage(self):
        if self.fotografia:
            return '{}{}'.format(MEDIA_URL, self.fotografia)
        else:
            return '{}{}'.format(STATIC_URL, 'img/OR.png')

    def toJSON(self):
        item = model_to_dict(self)
        return item


def set_organizacion(sender, instance, *args, **kwargs):
    if instance.nomorganizacion and not instance.abreviacion:
        aux = instance.nomorganizacion[:4]
        if Organizacion.objects.filter(abreviacion__exact=aux).exists():
            instance.abreviacion = '{}{}'.format(instance.nomorganizacion[:3], str(uuid.uuid4())[:2])
        else:
            instance.abreviacion = instance.nomorganizacion[:3]


pre_save.connect(set_organizacion, sender=Organizacion)


class Organizador(models.Model):
    user = models.OneToOneField(User, related_name="encargado_perfil", on_delete=models.CASCADE)
    organizacion = models.OneToOneField(Organizacion, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, blank=False, unique=True)
    avatar = models.ImageField(upload_to=fotoVoluntarios, null=True, blank=True, default='img/OR.png')

    def __str__(self):
        return f' {self.user.persona.Nombre}-{self.user.persona.Apellido}-{self.organizacion.abreviacion}'

    class Meta:
        verbose_name = _('Organizador')
        verbose_name_plural = _('Organizadores')
        db_table = 'Organizador'

    def get_image(self):
        if self.avatar:
            return '{}{}'.format(MEDIA_URL, self.avatar)
        else:
            return '{}{}'.format(STATIC_URL, 'img/Or.png')


def set_slug(sender, instance, *args, **kwargs):
    if instance.organizacion.abreviacion and not instance.slug:
        slug = slugify(
            '{}{}-{}'.format(instance.user.username[:4], instance.organizacion.abreviacion, str(uuid.uuid4())[:4])
        )

        instance.slug = slug


pre_save.connect(set_slug, sender=Organizador)


class Voluntario(models.Model):
    user = models.OneToOneField(User, related_name="voluntario_perfil", on_delete=models.CASCADE)
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=True, blank=True)
    retirado = models.BooleanField(default=False)
    fecha_retiro = models.DateField(null=True, blank=True)
    slug = models.SlugField(null=False, blank=False, unique=True)
    avatar = models.ImageField(upload_to=fotoVoluntarios, null=True, blank=True, default='img/Vol.png')

    def __str__(self):
        return f'{self.user.persona.Nombre}-{self.user.persona.Apellido}- {self.organizacion.nomorganizacion}'

    class Meta:
        verbose_name = _('Voluntario')
        verbose_name_plural = _('Voluntarios')
        db_table = 'Voluntario'

    def get_image(self):
        if self.avatar:
            return '{}{}'.format(MEDIA_URL, self.avatar)
        else:
            return '{}{}'.format(STATIC_URL, 'img/Vol.png')


def set_slug1(sender, instance, *args, **kwargs):
    if instance.organizacion.abreviacion and not instance.slug:
        slug = slugify(
            '{}{}-{}'.format(instance.user.username[:4], instance.organizacion.abreviacion, str(uuid.uuid4())[:4])
        )

        instance.slug = slug


pre_save.connect(set_slug1, sender=Voluntario)


class UsuarioReg(models.Model):
    user = models.OneToOneField(User, related_name="perfil_usuarioReg", on_delete=models.CASCADE)
    slug = models.SlugField(null=False, blank=False, unique=True)
    avatar = models.ImageField(upload_to=fotoUsuarioReg, null=True, blank=True, default='img/User.png')

    def __str__(self):
        return f' {self.user.username} {self.user.email}'

    class Meta:
        verbose_name = _('UsuarioRegistrado')
        verbose_name_plural = _('UsuariosRegistrados')
        db_table = 'UsuariosReg'

    def get_image(self):
        if self.avatar:
            return '{}{}'.format(MEDIA_URL, self.avatar)
        else:
            return '{}{}'.format(STATIC_URL, 'img/User.png')


def set_slug2(sender, instance, *args, **kwargs):
    if instance.user.username and not instance.slug:
        slug = slugify(
            '{}{}'.format(instance.user.username[:4], str(uuid.uuid4())[:4])
        )

        instance.slug = slug


pre_save.connect(set_slug2, sender=UsuarioReg)
