from rest_framework import serializers
from .models import Pessoa, Objeto, PossePessoaObjeto


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = '__all__'


class PossePessoaObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PossePessoaObjeto
        fields = '__all__'