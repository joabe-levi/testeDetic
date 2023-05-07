from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
import re
from utils.basics.models import BasicModel
from . import choices


class Pessoa(User):
    cpf = models.CharField(max_length=18, null=True, blank=True, unique=True)
    telefone = models.CharField(max_length=30, null=True, blank=True, unique=True)
    eh_policial = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        db_table = 'pessoa'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def limpa_cpf(self):
        return self.cpf.replace('-', '').replace('.', '')

    def save(self, *args, **kwargs):
        if not self.cpf.isnumeric():
            self.cpf = self.limpa_cpf()

        super().save()

    @staticmethod
    def valida_cpf(cpf):
        cpf = re.sub('[^0-9]', '', cpf)
        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = 11 - soma % 11
        if resto > 9:
            digito1 = '0'
        else:
            digito1 = str(resto)

        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = 11 - soma % 11
        if resto > 9:
            digito2 = '0'
        else:
            digito2 = str(resto)

        return cpf[-2:] == digito1 + digito2


class Objeto(BasicModel):
    descricao = models.TextField()
    tipo = models.IntegerField(choices=choices.CHOICES_TIPOS_OBJETOS)
    numero_serie = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    ano = models.PositiveSmallIntegerField(null=True, blank=True)
    cor = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Objeto'
        verbose_name_plural = 'Objetos'
        db_table = 'objeto'

    def __str__(self):
        return f'{self.descricao} - {self.get_tipo_display()}'


def consultar_arma(sender, **kwargs):
    instance = kwargs['instance']
    if instance.tipo == choices.CHOICE_ARMA:
        Arma.objects.get_or_create(objeto=instance)


post_save.connect(consultar_arma, sender=Objeto)


class PossePessoaObjeto(BasicModel):
    pessoa = models.ForeignKey(Pessoa, related_name='posses_por_pessoa', on_delete=models.PROTECT)
    objeto = models.ForeignKey(Objeto, related_name='posses_por_pessoa', on_delete=models.PROTECT)

    class Meta:
        unique_together = ('pessoa', 'objeto')

        verbose_name = 'Posse da Pessoa'
        verbose_name_plural = 'Posses de Pessoas'
        db_table = 'posse_pessoa_objeto'

    def __str__(self):
        return f'{self.objeto} - {self.pessoa}'


class Arma(BasicModel):
    objeto = models.ForeignKey(Objeto, related_name='armas', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Arma'
        verbose_name_plural = 'Armas'
        db_table = 'arma'

    def __str__(self):
        return f'{self.objeto}'


class RegistroOficialDeArma(BasicModel):
    arma = models.OneToOneField(Arma, related_name='registros_oficiais_armas', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Registro Oficial de Arma'
        verbose_name_plural = 'Registros Oficiais de Armas'
        db_table = 'registro_oficial_arma'

    def __str__(self):
        return f'{self.arma}'
