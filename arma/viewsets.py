from arma.filters import ArmaFilter, RegistroOficialArmaFilter
from arma.models import Arma, RegistroOficialDeArma
from arma.serializers import ArmaSerializer, RegistroOficialArmaSerializer
from core.basics.permissions.permissions import IsSuperUserOrReadOnly, IsPolicialOrReadOnly
from core.basics.viewsets.viewsets import BasicModelViewSet
from objeto import choices


class ArmaViewSet(BasicModelViewSet):
    filterset_class = ArmaFilter
    serializer_class = ArmaSerializer

    def get_queryset(self):
        return Arma.objects.select_related('objeto').filter(objeto__tipo=choices.CHOICE_ARMA)


class RegistroOficialArmaViewSet(BasicModelViewSet):
    filterset_class = RegistroOficialArmaFilter
    serializer_class = RegistroOficialArmaSerializer
    permission_classes = [IsPolicialOrReadOnly, IsSuperUserOrReadOnly]
    queryset = RegistroOficialDeArma.objects.filter(arma__objeto__tipo=choices.CHOICE_ARMA)
