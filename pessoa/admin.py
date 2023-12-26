from django.contrib import admin

from core.basics.admins.admins import BasicAdmin
from pessoa.models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(BasicAdmin):
    list_display = ('first_name', 'email', 'eh_policial',)
