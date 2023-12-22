from arma.filters import ArmaFilter
from arma.models import Arma
from arma.serializers import ArmaSerializer
from core.basics.viewsets.viewsets import BasicModelViewSet
from objeto import choices


class ArmaViewSet(BasicModelViewSet):
    filterset_class = ArmaFilter
    serializer_class = ArmaSerializer

    def get_queryset(self):
        return Arma.objects.select_related('objeto').filter(objeto__tipo=choices.CHOICE_ARMA)
