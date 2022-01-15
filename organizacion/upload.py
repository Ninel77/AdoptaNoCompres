from datetime import datetime, date
#from organizacion.models import AnimalesDatosB
'''
def docAdopcion(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #return f'{instance.user.voluntario_perfil.organizacion.abreviacion}/Animales/{instance.slug}/documentos' + filename
    #return f'{instance.animal.organizacion.abreviacion}/Animales/{instance.slug}/documentos' + filename
    slugAnimal = instance.slug
    animal = AnimalesDatosB.objects.get(slug=slugAnimal)
    organizacion = animal.organizacion.abreviacion
    return f'{organizacion}/Animales/{instance.slug}/documentos' + filename
'''
def fotoIngreso(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'{instance.animal.organizacion.abreviacion}/Animales/{instance.slug}/fotoIngreso/' + filename

def fotoPaAdopcion(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'{instance.animal.organizacion.abreviacion}/Animales/{instance.slug}/fotoPaAdopcion/' + filename

def fotoAdopcion(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'{instance.animal.organizacion.abreviacion}/Animales/{instance.slug}/fotoAdopcion/' + filename

def fotoSantuario(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'{instance.animal.organizacion.abreviacion}/Animales/{instance.slug}/fotoSantuario/' + filename

def age(birth_date):
    today = date.today()
    y = today.year - birth_date.year
    if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
        y -= 1
    return y

def rangoEdadAnimal(mesesEdad, anosEdad):
    edad_Anim = None
    if mesesEdad <= 2 and anosEdad == 0:
        edad_Anim = 'CACHORRO LACTANTE'
    elif mesesEdad > 2 and anosEdad < 1:
        edad_Anim = 'CACHORRO'
    elif anosEdad <= 4 and anosEdad >= 1:
        edad_Anim = 'JOVEN'
    elif anosEdad <= 7 and anosEdad > 4:
        edad_Anim = 'ADULTO'
    elif anosEdad > 7:
        edad_Anim = 'ADULTO SENIOR'

    return edad_Anim

def rangoEdadPersona(edad):
    rango_edad = None
    if edad >= 18 and edad <=20:
        rango_edad = 'ADOLECENTE'
    elif edad >=21 and edad <=25:
        rango_edad = 'JOVEN'
    elif edad >=26 and edad <=30:
        rango_edad = 'ADULTO JOVEN'
    elif edad >=31 and edad <=40:
        rango_edad = 'ADULTEZ PRIMARIA'
    elif edad >=41 and edad <=50:
        rango_edad = 'ADULTEZ INTERMEDIA'
    elif edad >=51 and edad <=60:
        rango_edad = 'ADULTEZ TARDIA'
    elif edad >=61 :
        rango_edad = 'ADULTO MAYOR'

    return rango_edad