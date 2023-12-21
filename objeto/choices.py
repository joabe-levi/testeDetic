CHOICE_ARMA = 1
CHOICE_CARRO = 2
CHOICE_COMPUTADOR = 3
CHOICE_VIATURA_POLICIAL = 4

CHOICES_TIPOS_OBJETOS = (
    (CHOICE_ARMA, 'Arma'),
    (CHOICE_CARRO, 'Carro'),
    (CHOICE_COMPUTADOR, 'Computador'),
    (CHOICE_VIATURA_POLICIAL, 'Viatura policial'),
)


class ChoiceTipoObjeto:
    def __init__(self, obj):
        self.object = obj

    @property
    def arma(self):
        return self.object.tipo == CHOICE_ARMA

    @property
    def carro(self):
        return self.object.tipo == CHOICE_CARRO

    @property
    def computador(self):
        return self.object.tipo == CHOICE_COMPUTADOR

    @property
    def viatura_policial(self):
        return self.object.tipo == CHOICE_VIATURA_POLICIAL
