from collections import OrderedDict

from rest_framework import serializers

from arma.models import Arma, RegistroOficialDeArma
from objeto.serializers import ObjetoSerializer


class ArmaSerializer(serializers.ModelSerializer):
    objeto = ObjetoSerializer()

    class Meta:
        model = Arma
        fields = ('id', 'objeto',)
        read_only_fields = ('id', 'uuid',)


class RegistroOficialArmaSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistroOficialDeArma
        fields = ('arma',)

    def to_representation(self, instance):
        dict_response = OrderedDict()
        objeto = instance.arma.objeto
        dict_response['id'] = instance.id
        dict_response['descricao'] = objeto.descricao
        dict_response['tipo'] = objeto.get_tipo_display()
        dict_response['numero_serie'] = objeto.numero_serie
        dict_response['modelo'] = objeto.modelo
        dict_response['ano'] = objeto.ano
        dict_response['cor'] = objeto.cor
        dict_response['ativo'] = instance.ativo
        return dict_response
