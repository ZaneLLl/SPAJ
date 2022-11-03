from aventura.models import aventuras
from django.db import models
from django.contrib.auth.models import User


class fichas(models.Model):
    nomePersonagem = models.CharField(max_length=45)
    historiaPersonagem = models.TextField(max_length=1000)
    Level = models.IntegerField(blank=False)
    Sabedoria = models.IntegerField(blank=False)
    Agilidade = models.IntegerField(blank=False)
    Conhecimento = models.IntegerField(blank=False)
    Destreza = models.IntegerField(blank=False)
    ConstFisica = models.IntegerField(blank=False)
    Percepção = models.IntegerField(blank=False)
    Carisma = models.IntegerField(blank=False)
    Vitalidade = models.IntegerField(default=0)
    Força = models.IntegerField(default=0)
    Luta = models.IntegerField(default=0)
    preencher_ficha = models.ManyToManyField(User)
    id_aventura = models.ForeignKey(aventuras, on_delete=models.CASCADE, blank=False)

class pericias(models.Model):
    nome_pericia = models.CharField(max_length=30, unique=True, blank=False)
    descrição_pericia = models.CharField(max_length=100)
    conter_pericia = models.ManyToManyField(fichas)

class equipamentos(models.Model):
    nome_equi = models.CharField(max_length=20, unique=True, blank=False)
    dano = models.IntegerField(blank=True, null=True)
    defesa = models.IntegerField(blank=True, null=True)
    descrição = models.CharField(max_length=100)


class possuir_equipamento(models.Model):
    id_equi = models.ForeignKey(equipamentos, on_delete=models.CASCADE)
    id_ficha = models.ForeignKey(fichas, on_delete=models.CASCADE)
    quantidade = models.IntegerField(blank=False, default= 0 )

