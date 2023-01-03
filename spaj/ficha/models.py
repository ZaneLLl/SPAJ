from django.db import models
from django.contrib.auth.models import User


class aventuras(models.Model):
    nomeAventura = models.CharField(max_length=100, null=False, unique=True, verbose_name= 'Nome Da Aventura:')
    guia_de_ambiente = models.CharField(max_length=100, blank=True, verbose_name= 'Guia De Ambiente:')
    historia_aventura = models.CharField(max_length=100, blank=True, verbose_name= 'Historia:')
    jogar_aventura = models.ManyToManyField(User, related_name='aventura')

    def __str__(self):
        return  self.nomeAventura

class pericias(models.Model):
    nome_pericia = models.CharField(max_length=30, unique=True, blank=False, verbose_name='Pericia')
    descrição_pericia = models.CharField(max_length=100, verbose_name='Descrição')
    atrib1 = models.IntegerField(default='1', blank=False, null=False)
    atrib2 = models.IntegerField(default='1', blank=False, null=False)
    combate = models.BooleanField(default='False', blank=False, null=False)
    def __str__(self):
        return self.nome_pericia

class equipamentos(models.Model):
    nome_equi = models.CharField(max_length=20, unique=True, blank=False)
    dano = models.IntegerField(blank=True, null=True)
    defesa = models.IntegerField(blank=True, null=True)
    descrição = models.CharField(max_length=100)
    combate = models.BooleanField(default='False', blank=False, null=False)
    def __str__(self):
        return self.nome_equi

class fichas(models.Model):
    nomePersonagem = models.CharField(max_length=45, verbose_name='Nome do Personagem', blank=False, null=False)
    historiaPersonagem = models.TextField(max_length=1000, verbose_name= 'Historia do Personagem')
    Level = models.IntegerField(blank=False)
    Sabedoria = models.IntegerField(blank=False)
    Agilidade = models.IntegerField(blank=False)
    Conhecimento = models.IntegerField(blank=False)
    Destreza = models.IntegerField(blank=False)
    ConstFisica = models.IntegerField(blank=False)
    Percepção = models.IntegerField(blank=False)
    Carisma = models.IntegerField(blank=False)
    Vitalidade = models.IntegerField(blank=False)
    Força = models.IntegerField(blank=False)
    Luta = models.IntegerField(blank=False)
    preencher_ficha = models.ManyToManyField(User, related_name='usuarios')
    id_aventura = models.ForeignKey(aventuras, on_delete=models.CASCADE, blank=False, verbose_name='Aventura')
    conter_pericia = models.ManyToManyField(pericias, related_name='conter_pericia', verbose_name='Pericias', blank=True)
    possuir_equipamento = models.ManyToManyField(equipamentos, related_name='possuir_equipamento', verbose_name='Equipamentos', blank=True )

    def __str__(self):
        return '{}. {}'.format(self.id, self.nomePersonagem)








