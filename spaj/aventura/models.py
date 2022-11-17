from django.db import models
from django.contrib.auth.models import User

class aventuras(models.Model):
    nomeAventura = models.CharField(max_length=100, null=False, unique=True)
    guia_de_ambiente = models.CharField(max_length=100, blank=True)
    historia_aventura = models.CharField(max_length=100, blank=True)
    jogar_aventura = models.ManyToManyField(User)

    def __str__(self):
        return '{}. {}'.format(self.id, self.nomeAventura)