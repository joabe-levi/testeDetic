from rest_framework.viewsets import ModelViewSet

from arma.filters import ArmaFilter
from arma.models import Arma
from arma.serializers import ArmaSerializer


class ArmaViewSet(ModelViewSet):
    queryset = Arma.objects.all()
    filterset_class = ArmaFilter
    serializer_class = ArmaSerializer