from rest_framework import serializers

from arma.models import Arma
from objeto.serializers import ObjetoSerializer


class ArmaSerializer(serializers.ModelSerializer):
    objeto = ObjetoSerializer()

    class Meta:
        model = Arma
        fields = ('objeto',)
        read_only_fields = ('id', 'uuid',)
