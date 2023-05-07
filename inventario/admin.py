from django.contrib import admin
from . import models


admin.site.register(models.Pessoa)
admin.site.register(models.Objeto)
admin.site.register(models.PossePessoaObjeto)
admin.site.register(models.RegistroOficialDeArma)