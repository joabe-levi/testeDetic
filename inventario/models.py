from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.basics.models import BasicModel
from . import choices


class Pessoa(AbstractUser):
    cpf = models.CharField(max_length=18, null=True, blank=True, unique=True)
    telefone = models.CharField(max_length=30, null=True, blank=True, unique=True)
    eh_policial = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        db_table = 'pessoa'


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
