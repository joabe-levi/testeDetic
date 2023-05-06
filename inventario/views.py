from django.views.generic.base import View
from django.shortcuts import redirect
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .filters import PessoaFilter
from .models import Pessoa, Objeto, PossePessoaObjeto
from .serializers import PessoaSerializer, ObjetoSerializer, PossePessoaObjetoSerializer


class IndexView(View):
    def get(self, request):
        return redirect('overview/')


class ApiOverview(APIView):
    permission_classes = [AllowAny]
    queryset = None
    """
    Lista de todos os endpoints disponiveis
    """

    def get(self, request, format=None):
        api_urls = {
            'Objetos': {
                'list': 'api/objetos/',
                # 'detail': 'api/objetos/<int:pk>/',
                'create': 'api/objetos/incluir/',
                'update': 'api/objetos/<int:pk>/update/',
                'delete': 'api/objetos/<int:pk>/delete/',
            },
            'Pessoas': {
                'list': 'api/pessoas/',
                'create': 'api/pessoas/create/',
                'update': 'api/pessoas/atualizar/<int:pk>',
                'delete': 'api/pessoas/excluir/<int:pk>/',
            },
            'PossePessoaObjeto': {
                'list': 'api/posse_pessoa_objetos/',
                'detail': 'api/posse_pessoa_objetos/<int:pk>/',
                'create': 'api/posse_pessoa_objetos/create/',
                'update': 'api/posse_pessoa_objetos/<int:pk>/update/',
                'delete': 'api/posse_pessoa_objetos/<int:pk>/delete/',
            }
        }

        return Response(api_urls, status=status.HTTP_200_OK)


class PessoaListView(generics.ListAPIView):
    queryset = Pessoa.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = PessoaFilter
    serializer_class = PessoaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        filter_qs = dict()
        if self.request.query_params:
            filter_qs = self.request.query_params.dict()

        return Pessoa.objects.filter(**filter_qs)


class PessoaCreateView(generics.CreateAPIView):
    serializer_class = PessoaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cpf = serializer.data.get('cpf')
        if Pessoa.valida_cpf(cpf):
            # TODO Posteriormente criar mecanica de limpar cpf para remoção de caracteres
            super().perform_create(serializer)


class PessoaUpdateView(generics.UpdateAPIView):
    serializer_class = PessoaSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Pessoa.objects.get(pk=self.kwargs['pk'])

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PessoaDeleteView(generics.DestroyAPIView):
    serializer_class = PessoaSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Pessoa.objects.get(pk=self.kwargs['pk'])




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