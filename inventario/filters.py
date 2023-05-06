import django_filters
from inventario.models import Pessoa


class PessoaFilter(django_filters.FilterSet):

    class Meta:
        model = Pessoa
        fields = ('cpf', 'username', 'first_name', 'last_name')
        search_fields = ('cpf', 'username', 'first_name__icontains', 'last_name__icontains')