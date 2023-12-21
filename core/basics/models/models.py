import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords
from core.basics.models import choices
from core.basics.models.managers import BasicModelManager


class BasicModel(models.Model):
    uuid = models.UUIDField(verbose_name=_('UUID'), default=uuid.uuid4, editable=False, unique=True)

    data_criacao = models.DateTimeField(verbose_name=_('Data de criação'), auto_now_add=True, null=True, blank=True)
    data_modificacao = models.DateTimeField(verbose_name=_('Data de modificação'), auto_now=True, null=True, blank=True)
    origem_dados = models.IntegerField(
        verbose_name=_('Origem dos dados'), choices=choices.CHOICE_ORIGEM_DADOS, default=choices.ORIGEM_DADO_MANUAL,
        null=True, blank=True
    )
    ativo = models.BooleanField(verbose_name=_('Ativo'), default=True)
    history = HistoricalRecords(inherit=True)

    objects = BasicModelManager.as_manager()

    class Meta:
        abstract = True
