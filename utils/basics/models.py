import uuid
from django.db import models
from simple_history.models import HistoricalRecords

from utils.basics import choices


class BasicModel(models.Model):
    basic_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    data_criacao = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    data_modificacao = models.DateTimeField(auto_now=True, null=True, blank=True)
    origem_dados = models.IntegerField(
        choices=choices.CHOICE_ORIGEM_DADOS, default=choices.ORIGEM_DADO_MANUAL,
        null=True, blank=True
    )
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
