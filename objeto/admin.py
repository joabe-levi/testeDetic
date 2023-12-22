from django.contrib import admin

from core.basics.models.managers import BasicManagerDefault
from objeto.models import Objeto, PossePessoaObjeto


admin.site.register(PossePessoaObjeto)


@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'get_tipo_display', 'modelo',)

    def get_queryset(self, request):
        Objeto.add_to_class('objects', BasicManagerDefault.as_manager())
        return super().get_queryset(request)
