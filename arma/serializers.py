from rest_framework import serializers

from arma.models import Arma, RegistroOficialDeArma
from objeto.serializers import ObjetoSerializer


class ArmaSerializer(serializers.ModelSerializer):
    objeto = ObjetoSerializer()

    class Meta:
        model = Arma
        fields = ('objeto',)
        read_only_fields = ('id', 'uuid',)


class RegistroOficialArmaSerializer(serializers.ModelSerializer):
    # arma = ArmaSerializer()

    class Meta:
        model = RegistroOficialDeArma
        fields = ('arma',)
        # read_only_fields = ('__all__',)
