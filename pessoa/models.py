import re
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models


class Pessoa(User):
    cpf = models.CharField(verbose_name=_('CPF'), max_length=18, null=True, blank=True, unique=True)
    telefone = models.CharField(verbose_name=_('Telefone'), max_length=30, null=True, blank=True, unique=True)
    eh_policial = models.BooleanField(verbose_name=_('É policial'), default=False)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        db_table = 'pessoa'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def limpa_cpf(self):
        return self.cpf.replace('-', '').replace('.', '')

    def save(self, *args, **kwargs):
        if not self.cpf.isnumeric():
            self.cpf = self.limpa_cpf()

        super().save()

    @staticmethod
    def valida_cpf(cpf):
        cpf = re.sub('[^0-9]', '', cpf)
        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = 11 - soma % 11
        if resto > 9:
            digito1 = '0'
        else:
            digito1 = str(resto)

        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = 11 - soma % 11
        if resto > 9:
            digito2 = '0'
        else:
            digito2 = str(resto)

        return cpf[-2:] == digito1 + digito2
