import django_filters
from pessoa.models import Pessoa


class PessoaFilter(django_filters.FilterSet):

    class Meta:
        model = Pessoa
        fields = ('cpf', 'username', 'first_name', 'last_name')
