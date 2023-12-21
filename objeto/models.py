from django.db import models
from django.db.models.signals import post_save

from django.utils.translation import gettext_lazy as _

from arma.models import Arma
from pessoa.models import Pessoa
from core.basics.models.models import BasicModel
from . import choices


class Objeto(BasicModel):
    descricao = models.TextField(verbose_name=_('Descrição'))
    tipo = models.IntegerField(verbose_name=_('Tipo'), choices=choices.CHOICES_TIPOS_OBJETOS)
    numero_serie = models.CharField(verbose_name=_('Número de Série'), max_length=50, null=True, blank=True)
    modelo = models.CharField(verbose_name=_('Modelo'), max_length=50, null=True, blank=True)
    ano = models.PositiveSmallIntegerField(verbose_name=_('Ano'), null=True, blank=True)
    cor = models.CharField(verbose_name=_('Cor'), max_length=50, null=True, blank=True)

    _tipo_objeto = None

    class Meta:
        verbose_name = 'Objeto'
        verbose_name_plural = 'Objetos'
        db_table = 'objeto'

    def __str__(self):
        return f'{self.descricao} - {self.get_tipo_display()}'

    @property
    def tipo_objeto(self):
        if not self._tipo_objeto:
            self._tipo_objeto = choices.ChoiceTipoObjeto(self)
        return self._tipo_objeto


def consultar_arma(sender, **kwargs):
    instance = kwargs['instance']
    if instance.tipo_objeto.arma:
        Arma.objects.get_or_create(objeto=instance)


post_save.connect(consultar_arma, sender=Objeto)


class PossePessoaObjeto(BasicModel):
    pessoa = models.ForeignKey(
        Pessoa, related_name='posses_por_pessoa', on_delete=models.PROTECT, verbose_name=_('Pessoa')
    )
    objeto = models.ForeignKey(
        Objeto, related_name='posses_por_pessoa', on_delete=models.PROTECT, verbose_name=_('Objeto')
    )

    class Meta:
        unique_together = ('pessoa', 'objeto',)

        verbose_name = 'Posse da Pessoa'
        verbose_name_plural = 'Posses de Pessoas'
        db_table = 'posse_pessoa_objeto'

    def __str__(self):
        return f'{self.objeto} - {self.pessoa}'
