from django.test import TestCase

# Create your tests here.

'''
infoRes = AnimalesRescatados.objects.get(slug=slug)
                    fecha_Res = infoRes.Fecha_Rescate,
                    dias = adopAnim.fechaRegistroAdop.day - infoRes.Fecha_Rescate.day
                    print('dias adop', dias)
                    especie = form1.cleaned_data['especie']
                    print(especie, ':especie')
                    raza = form1.cleaned_data['raza']
                    print(raza, ':raza')
                    color2 = form1.cleaned_data['color2']
                    print(color2, ':color2')
                    color1 = form1.cleaned_data['color1']
                    print(color1, ':color1')

                    ester = form5.cleaned_data['esterilizacion']
                    print(ester, ':ester')
                    discT = form5.cleaned_data['discapacidad']
                    
                    if discT == True:                        
                        disc = 'NINGUNO'
                    else:
                        disc = form5.cleaned_data['Tipodiscapacidad']
                    print(disc, ':disc')

                    sex_p = form3.cleaned_data['Genero']
                    print(sex_p, ':sex_p')

                    data = Dataset.objects.create(
                        edadAnos=adopAnim.edadAnos,
                        edadMeses=adopAnim.edadMeses,
                        edad_anim=str(edadAnimal),
                        especie_anim=especie,
                        raza_anim=raza,
                        tamano_anim=datAnim.tamano,
                        sexo_anim=datAnim.sexo,
                        color_prin=color1,
                        color_sec=color2,
                        esterilizacion=ester,
                        f_rescate=fecha_Res,
                        f_adopcion=adopAnim.fechaRegistroAdop,
                        diasEnAdop=dias,
                        edad_adop=edadActual,
                        rangoEdad=rangoEdadAdop,
                        sexo_adop=sex_p,
                        ocupacion=adoptantes.ocupacion,
                        tipo_vivienda_adop=adoptantes.tipo_vivienda,
                        Tipodiscapacidad=disc,
                    )
                    data.save()
'''
