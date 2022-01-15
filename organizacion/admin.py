from django.contrib import admin

from .models import (AnimalesAdoptados, DocumentosAdopcion, Especie, Raza, Color, AnimalesRescatados,
                     AnimalesEnAdopcion, AnimalesDatosB, InfoEvaluacion, Adoptante)


# Register your models here.


class AnimDatosB(admin.ModelAdmin):
    fields = (
        'nombre', 'especie', 'raza', 'tamano', 'sexo', 'color1', 'color2', 'organizacion', 'estado', 'descripcion',
        )
    list_display = ('__str__', 'slug')


class AnimRes(admin.ModelAdmin):
    fields = ('animal', 'edadAnos', 'edadMeses', 'fotoRescate', 'descripcionRescate',
              'voluntarioAcargo', 'Fecha_Rescate', 'FechaRegistro')
    list_display = ('__str__', 'slug')


class AnimAdo(admin.ModelAdmin):
    fields = ('animal', 'adoptante', 'documentos', 'voluntarioAcargo', 'edadAnos', 'edadMeses', 'fotoAdopcion',
              'descripcionAdop', 'fechaRegistroAdop')
    list_display = ('__str__', 'slug')


class AnimEnA(admin.ModelAdmin):
    fields = ('animal', 'voluntarioAcargo', 'edadAnos', 'edadMeses',
              'fecha_en_Adopcion', 'fotoEnAdopcion', 'descripcionEnAdop')
    list_display = ('__str__', 'slug')


admin.site.register(Especie)
admin.site.register(Raza)
admin.site.register(Color)
admin.site.register(InfoEvaluacion)
admin.site.register(AnimalesDatosB, AnimDatosB)
admin.site.register(AnimalesRescatados, AnimRes)
admin.site.register(AnimalesAdoptados, AnimAdo)
admin.site.register(AnimalesEnAdopcion, AnimEnA)
admin.site.register(Adoptante)
admin.site.register(DocumentosAdopcion)
