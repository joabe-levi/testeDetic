from core.basics.viewsets.viewsets import BasicModelViewSet
from objeto.filters import ObjetoFilter, PossePorPessoaFilter
from objeto.models import Objeto, PossePessoaObjeto
from objeto.serializers import ObjetoSerializer, PossePessoaObjetoToListSerializer


class ObjetoViewSet(BasicModelViewSet):
    queryset = Objeto.objects.all()
    filterset_class = ObjetoFilter
    serializer_class = ObjetoSerializer


class PossePessoaObjetoViewSet(BasicModelViewSet):
    queryset = PossePessoaObjeto.objects.all()
    filterset_class = PossePorPessoaFilter
    serializer_class = PossePessoaObjetoToListSerializer
