import django_filters
from arma.models import Arma


class ArmaFilter(django_filters.FilterSet):
    class Meta:
        model = Arma
        fields = ('objeto__descricao',)
