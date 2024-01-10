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
