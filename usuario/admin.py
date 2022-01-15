from django.contrib import admin

# Register your models here.
from .models import User, Organizacion, Organizador, UsuarioReg, Voluntario, DatosPersonales, SuperUser


class UserIn(admin.ModelAdmin):
    fields = ('persona', 'username', 'email', 'password', 'rol', 'is_staff', 'is_active',
              'is_superuser', 'is_organizador', 'is_voluntario', 'is_userr')
    list_display = ('__str__', 'rol')

class Organizadores(admin.ModelAdmin):
    fields = ('user', 'organizacion')
    list_display = ('__str__', 'slug')

class Voluntarios(admin.ModelAdmin):
    fields = ('user', 'Organizacion', 'fecha_inicio', )
    list_display = ('__str__', 'slug')

class UserReg(admin.ModelAdmin):
    fields = ('user', 'avatar')
    list_display = ('__str__', 'slug')

class UserAdmi(admin.ModelAdmin):
    fields = ('user', 'avatar')
    list_display = ('__str__', 'slug')


admin.site.register(SuperUser, UserAdmi)
admin.site.register(User, UserIn)
admin.site.register(Organizacion)
admin.site.register(Organizador, Organizadores)
admin.site.register(UsuarioReg, UserReg)
admin.site.register(Voluntario, Voluntarios)
admin.site.register(DatosPersonales)