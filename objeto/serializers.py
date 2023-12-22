from rest_framework import serializers

from arma.models import RegistroOficialDeArma
from objeto.models import Objeto, PossePessoaObjeto
from pessoa.serializers import PessoaSerializer


class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = ('id', 'descricao', 'tipo', 'numero_serie', 'modelo', 'ano', 'cor',)
        read_only_fields = ('id', 'uuid',)


class PossePessoaObjetoToListSerializer(serializers.ModelSerializer):
    pessoa = PessoaSerializer()
    objeto = ObjetoSerializer()

    class Meta:
        model = PossePessoaObjeto
        fields = ('objeto', 'pessoa',)


class PossePessoaObjetoToActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PossePessoaObjeto
        fields = ('objeto', 'pessoa',)

    def validate(self, data):
        objeto = data.get('objeto')
        pessoa = data.get('pessoa')

        if objeto.tipo_objeto.carro or objeto.tipo_objeto.viatura_policial:
            outras_posses = PossePessoaObjeto.objects.filter(objeto=objeto)

            policiais_possuindo = outras_posses.filter(pessoa__eh_policial=True)

            if objeto.tipo_objeto.viatura_policial and not pessoa.eh_policial:
                raise serializers.ValidationError(
                    'Somente policiais civis podem possuir objetos do tipo viatura policial!'
                )

            if policiais_possuindo.count() >= 2:
                raise serializers.ValidationError(
                    'Apenas duas pessoas policiais civis podem possuir objetos do tipo viatura policial!'
                )
        if objeto.tipo_objeto.arma:
            if not RegistroOficialDeArma.objects.filter(arma__objeto=objeto).exists():
                raise serializers.ValidationError('Esta arma não consta na tabela de registros oficiais!')

        else:
            outras_posses = PossePessoaObjeto.objects.filter(objeto=objeto)

            if outras_posses.count() >= 1:
                raise serializers.ValidationError(
                    'Objetos desse tipo só podem ser possuídos por uma pessoa por vez!'
                )
        return data
