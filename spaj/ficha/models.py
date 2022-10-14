from django.db import models
from django.contrib.auth.models import User

class fichas(models.Model):
    nomePersonagem = models.CharField(max_length=45)
    historiaPersonagem = models.TextField(max_length=1000)
    LVL = models.IntegerField(blank=False)
    SAB = models.IntegerField(blank=False)
    AGL = models.IntegerField(blank=False)
    CON = models.IntegerField(blank=False)
    DES = models.IntegerField(blank=False)
    CTF = models.IntegerField(blank=False)
    PER = models.IntegerField(blank=False)
    CAR = models.IntegerField(blank=False)
    VIT = models.IntegerField(default=0)
    FOR = models.IntegerField(default=0)
    LUT = models.IntegerField(default=0)
    user = models.IntegerField(blank=False)




