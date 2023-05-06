from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
import re

from utils.basics.models import BasicModel
from . import choices


class Pessoa(User):
    cpf = models.CharField(max_length=18, null=True, blank=True, unique=True)
    telefone = models.CharField(max_length=30, null=True, blank=True, unique=True)
    eh_policial = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        db_table = 'pessoa'

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


class Objeto(BasicModel):
    descricao = models.TextField()
    tipo = models.IntegerField(choices=choices.CHOICES_TIPOS_OBJETOS)
    numero_serie = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    ano = models.PositiveSmallIntegerField(null=True, blank=True)
    cor = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Objeto'
        verbose_name_plural = 'Objetos'
        db_table = 'objeto'


class PossePessoaObjeto(BasicModel):
    pessoa = models.ForeignKey(Pessoa, related_name='posses_por_pessoa', on_delete=models.PROTECT)
    objeto = models.ForeignKey(Objeto, related_name='posses_por_pessoa', on_delete=models.PROTECT)
    eh_de_policia = models.BooleanField(default=False)

    class Meta:
        unique_together = ('pessoa', 'objeto')

        verbose_name = 'Posse da Pessoa'
        verbose_name_plural = 'Posses da Pessoa'
        db_table = 'posse_pessoa_objeto'

    def save(self, *args, **kwargs):
        if self.eh_de_policia and not self.pessoa.eh_policial:
            raise ValidationError('Somente policiais devem possuir objetos desse tipo!')
        super().save(*args, **kwargs)
