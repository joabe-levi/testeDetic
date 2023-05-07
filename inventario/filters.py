import django_filters
from inventario.models import Pessoa, Objeto, PossePessoaObjeto


class PessoaFilter(django_filters.FilterSet):

    class Meta:
        model = Pessoa
        fields = ('cpf', 'username', 'first_name', 'last_name')


class ObjetoFilter(django_filters.FilterSet):
    class Meta:
        model = Objeto
        fields = ('descricao', 'numero_serie', 'modelo', 'ano', 'cor')


class PossePorPessoaFilter(django_filters.FilterSet):
    class Meta:
        model = PossePessoaObjeto
        fields = ('pessoa__cpf', 'pessoa__username', 'pessoa__first_name', 'pessoa__last_name')
