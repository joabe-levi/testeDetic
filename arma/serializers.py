from rest_framework import serializers

from arma.models import Arma


class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = ('__all__',)
        read_only_fields = ('id', 'uuid',)
