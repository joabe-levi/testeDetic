from django.views.generic.base import View
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from objeto.models import Objeto, PossePessoaObjeto
from objeto.serializers import ObjetoSerializer, PossePessoaObjetoToListSerializer, PossePessoaObjetoToActionSerializer
from pessoa.models import Pessoa
from pessoa.serializers import PessoaSerializer
from utils.basics.basic_permissions.permissions import IsPolicialOrReadOnly
from . import filters as filter_inventario


class IndexView(View):
    def get(self, request):
        return redirect('overview/')


class ApiOverview(APIView):
    permission_classes = [AllowAny]
    queryset = None
    """
    Lista de todos os endpoints disponiveis
    """

    def get(self, request, *args, **kwargs):
        api_urls = {
            'Objetos': {
                'list': 'api/objetos/',
                'create': 'api/objetos/incluir/',
                'update': 'api/objetos/atualizar/<int:pk>/',
                'delete': 'api/objetos/excluir/<int:pk>/',
            },
            'Pessoas': {
                'list': 'api/pessoas/',
                'create': 'api/pessoas/incluir/',
                'update': 'api/pessoas/atualizar/<int:pk>',
                'delete': 'api/pessoas/excluir/<int:pk>/',
            },
            'PossePessoaObjeto': {
                'list': 'api/posses/',
                'create': 'api/posses/incluir/',
                'update': 'api/posses/atualizar/<int:pk>/',
                'delete': 'api/posses/excluir/<int:pk>/',
            }
        }

        return Response(api_urls, status=status.HTTP_200_OK)


class PessoaListView(generics.ListAPIView):
    queryset = Pessoa.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = filter_inventario.PessoaFilter
    serializer_class = PessoaSerializer
    permission_classes = [IsPolicialOrReadOnly]


class PessoaCreateView(generics.CreateAPIView):
    serializer_class = PessoaSerializer
    permission_classes = [IsPolicialOrReadOnly]


class PessoaUpdateView(generics.UpdateAPIView):
    serializer_class = PessoaSerializer
    permission_classes = [IsPolicialOrReadOnly]

    def get_object(self):
        return Pessoa.objects.get(pk=self.kwargs['pk'])


class PessoaDeleteView(generics.DestroyAPIView):
    serializer_class = PessoaSerializer
    permission_classes = [IsPolicialOrReadOnly]

    def get_object(self):
        return Pessoa.objects.get(pk=self.kwargs['pk'])


#############################################################################
class ObjetoListView(generics.ListAPIView):
    queryset = Objeto.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = filter_inventario.ObjetoFilter
    serializer_class = ObjetoSerializer
    permission_classes = [IsPolicialOrReadOnly]


class ObjetoCreateView(generics.CreateAPIView):
    serializer_class = ObjetoSerializer
    permission_classes = [IsPolicialOrReadOnly]


class ObjetoUpdateView(generics.UpdateAPIView):
    serializer_class = ObjetoSerializer
    permission_classes = [IsPolicialOrReadOnly]

    def get_object(self):
        return Objeto.objects.get(id=self.kwargs.get('pk'))


class ObjetoDeleteView(generics.DestroyAPIView):
    serializer_class = PessoaSerializer
    permission_classes = [IsPolicialOrReadOnly]

    def get_object(self):
        return Objeto.objects.get(pk=self.kwargs['pk'])


#############################################################################
class PossePessoaObjetoListView(generics.ListAPIView):
    queryset = PossePessoaObjeto.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = filter_inventario.PossePorPessoaFilter
    serializer_class = PossePessoaObjetoToListSerializer
    permission_classes = [IsPolicialOrReadOnly]


class PossePessoaObjetoCreateView(generics.CreateAPIView):
    serializer_class = PossePessoaObjetoToActionSerializer
    permission_classes = [IsPolicialOrReadOnly]


class PossePessoaObjetoUpdateView(generics.UpdateAPIView):
    serializer_class = ObjetoSerializer
    permission_classes = [IsPolicialOrReadOnly]


class PossePessoaObjetoDeleteView(generics.DestroyAPIView):
    serializer_class = ObjetoSerializer
    permission_classes = [IsPolicialOrReadOnly]
