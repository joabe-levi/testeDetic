import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords
from utils.basics import choices


class BasicModel(models.Model):
    basic_id = models.UUIDField(verbose_name=_('UUID'), default=uuid.uuid4, editable=False, unique=True)

    data_criacao = models.DateTimeField(verbose_name=_('Data de criação'), auto_now_add=True, null=True, blank=True)
    data_modificacao = models.DateTimeField(verbose_name=_('Data de modificação'), auto_now=True, null=True, blank=True)
    origem_dados = models.IntegerField(
        verbose_name=_('Origem dos dados'), choices=choices.CHOICE_ORIGEM_DADOS, default=choices.ORIGEM_DADO_MANUAL,
        null=True, blank=True
    )
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
