from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Pessoa, Objeto, PossePessoaObjeto
from .serializers import PessoaSerializer, ObjetoSerializer, PossePessoaObjetoSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [IsAuthenticated]


class ObjetoViewSet(viewsets.ModelViewSet):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer
    permission_classes = [IsAuthenticated]


class PossePessoaObjetoViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = PossePessoaObjeto.objects.all()
    serializer_class = PossePessoaObjetoSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def transferir_posse(self, request, pk=None):
        posse = self.get_object()
        posse.eh_de_policia = not posse.eh_de_policia
        posse.save()
        return Response(self.serializer_class(posse).data)