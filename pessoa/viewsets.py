from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from inventario import filters as filter_inventario
from pessoa.models import Pessoa
from pessoa.serializers import PessoaSerializer
from utils.basics.permissions import IsPolicialOrReadOnly
from rest_framework import status
from rest_framework.response import Response


class PessoaViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = filter_inventario.PessoaFilter
    serializer_class = PessoaSerializer
    permission_classes = [IsPolicialOrReadOnly]

    def perform_create(self, serializer):
        cpf = serializer.validated_data.get('cpf')
        if Pessoa.valida_cpf(cpf):
            data = {
                'message': 'Objeto criado com sucesso!',
            }
            status_data = status.HTTP_201_CREATED
            super().perform_create(serializer)
        else:
            data = {
                'message': 'Cpf informado não é valido!',
            }
            status_data = status.HTTP_400_BAD_REQUEST

        return Response(data, status=status_data)
