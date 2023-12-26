import django_filters
from arma.models import Arma, RegistroOficialDeArma


class ArmaFilter(django_filters.FilterSet):
    descricao = django_filters.CharFilter(field_name='objeto__descricao', lookup_expr='icontains')

    class Meta:
        model = Arma
        fields = ('descricao',)


class RegistroOficialArmaFilter(django_filters.FilterSet):
    descricao = django_filters.CharFilter(field_name='arma__objeto__descricao', lookup_expr='icontains')

    class Meta:
        model = RegistroOficialDeArma
        fields = ('descricao',)
