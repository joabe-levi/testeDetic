from django.contrib import admin
from arma.models import Arma, RegistroOficialDeArma
from core.basics.admins.admins import BasicAdmin


@admin.register(Arma)
class ArmaAdmin(BasicAdmin):
    list_display = ('objeto', 'ativo',)


@admin.register(RegistroOficialDeArma)
class RegistroOficialDeArmaAdmin(BasicAdmin):
    list_display = ('arma', 'ativo',)
