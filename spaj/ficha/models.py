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


class preencher_ficha:
    id_ficha = models.ForeignKey(fichas,  primary_key=True, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

