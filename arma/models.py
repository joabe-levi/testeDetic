from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.basics.models import BasicModel
from objeto.models import Objeto


class Arma(BasicModel):
    objeto = models.ForeignKey(Objeto, related_name='armas', on_delete=models.PROTECT, verbose_name=_('Objeto'))

    class Meta:
        verbose_name = 'Arma'
        verbose_name_plural = 'Armas'
        db_table = 'arma'

    def __str__(self):
        return f'{self.objeto}'


class RegistroOficialDeArma(BasicModel):
    arma = models.OneToOneField(
        Arma, related_name='registros_oficiais_armas', on_delete=models.CASCADE, verbose_name=_('Arma')
    )

    class Meta:
        verbose_name = 'Registro Oficial de Arma'
        verbose_name_plural = 'Registros Oficiais de Armas'
        db_table = 'registro_oficial_arma'

    def __str__(self):
        return f'{self.arma}'
