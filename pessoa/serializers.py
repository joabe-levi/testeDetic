from rest_framework import serializers
from .models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)

    class Meta:
        model = Pessoa
        fields = '__all__'

    def create(self, validated_data):
        cpf = validated_data.get('cpf')
        if not Pessoa.valida_cpf(cpf):
            raise serializers.ValidationError("Cpf informado não é valido!")

        super().create(validated_data)
