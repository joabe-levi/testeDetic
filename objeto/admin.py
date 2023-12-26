from django.contrib import admin

from core.basics.admins.admins import BasicAdmin
from objeto.models import Objeto, PossePessoaObjeto


admin.site.register(PossePessoaObjeto)


@admin.register(Objeto)
class ObjetoAdmin(BasicAdmin):
    list_display = ('descricao', 'tipo_display', 'modelo', 'ativo')

    def tipo_display(self, obj):
        return obj.get_tipo_display()

    tipo_display.short_description = 'Tipo de objeto'
