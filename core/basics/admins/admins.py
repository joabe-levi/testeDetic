from django.contrib import admin

from core.basics.models.managers import BasicManagerDefault


class BasicAdmin(admin.ModelAdmin):
    actions = ['_atualizar_status_ativo', '_atualizar_status_inativo']

    @admin.display(description='Desativar registros')
    def _atualizar_status_inativo(self, request, queryset):
        queryset.update(ativo=False)

    @admin.display(description='Ativar registros')
    def _atualizar_status_ativo(self, request, queryset):
        queryset.update(ativo=True)

    def get_queryset(self, request):
        self.model.add_to_class('objects', BasicManagerDefault.as_manager())
        return super().get_queryset(request)
