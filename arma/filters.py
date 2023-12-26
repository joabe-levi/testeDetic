import django_filters
from arma.models import Arma, RegistroOficialDeArma


class ArmaFilter(django_filters.FilterSet):
    class Meta:
        model = Arma
        fields = ('objeto__descricao',)


class RegistroOficialArmaFilter(django_filters.FilterSet):
    class Meta:
        model = RegistroOficialDeArma
        fields = ('arma__objeto__descricao',)
