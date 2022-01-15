from django.contrib import admin

# Register your models here.

from MotorEmparejamiento.models import Form_C_preferencia, Form_S_preferencia, Dataset

admin.site.register(Form_C_preferencia)
admin.site.register(Form_S_preferencia)
admin.site.register(Dataset)
