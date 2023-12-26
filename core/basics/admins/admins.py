from django.contrib import admin

from core.basics.models.managers import BasicManagerDefault


def _atualizar_status_ativo(modeladmin, request, queryset):
    queryset.update(ativo=True)


def _atualizar_status_inativo(modeladmin, request, queryset):
    queryset.update(ativo=False)


_atualizar_status_ativo.short_description = 'Ativar registros'
_atualizar_status_inativo.short_description = 'Desativar registros'


class BasicAdmin(admin.ModelAdmin):
    actions = [_atualizar_status_ativo, _atualizar_status_inativo]

    def get_queryset(self, request):
        self.model.add_to_class('objects', BasicManagerDefault.as_manager())
        return super().get_queryset(request)
