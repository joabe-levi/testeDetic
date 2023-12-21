from pessoa.filters import PessoaFilter
from pessoa.models import Pessoa
from pessoa.serializers import PessoaSerializer
from rest_framework import status
from rest_framework.response import Response

from core.basics.viewsets.viewsets import BasicModelViewSet


class PessoaViewSet(BasicModelViewSet):
    queryset = Pessoa.objects.all()
    filterset_class = PessoaFilter
    serializer_class = PessoaSerializer

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
