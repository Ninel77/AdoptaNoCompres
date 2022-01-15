def fotoSuperUsuario(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'SuperUsuarios/{instance.slug}/' + filename

def logoOrganizacion(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'{instance.abreviacion}/logo/' + filename

def fotoVoluntarios(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'{instance.organizacion.abreviacion}/voluntarios/{instance.slug}/' + filename

def fotoUsuarioReg(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'userReg/{instance.slug}/fotoPerfil' + filename
