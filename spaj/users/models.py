from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class mestre(models.Model):
    nomeMestre = models.CharField(max_length=50,blank=False, null=False)
    emailMestre = models.CharField(max_length=100, unique=True)
    senhaMestre = models.CharField(max_length=255,blank=False, null=False)


class jogador(models.Model):
    nomeJogador = models.CharField(max_length=50,blank=False, null=False)
    emailJogador = models.CharField(max_length=100, unique=True)
    senhaJogador = models.CharField(max_length=255,blank=False, null=False)
