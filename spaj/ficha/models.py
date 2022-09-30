from django.db import models
from django.contrib.auth.models import User

class fichas(models.Model):
    nomePersonagem = models.CharField(max_length=45)
    historiaPersonagem = models.TextField(max_length=1000)
    #lvl = (('1','1'), ('2','2'),('3','3'), ('4','4'), ('5','5'), ('6','6'),('7','7'), ('8','8'),('9','9'), ('10','10'),('11','11') , ('12','12'),('13','13'), ('14','14'),('15','15'), ('16','16'), ('17','17'))
    LVL = models.CharField(max_length=2)
    SAB = models.CharField(max_length=2)
    AGL = models.CharField(max_length=2)
    CON = models.CharField(max_length=2)
    DES = models.CharField(max_length=2)
    CTF = models.CharField(max_length=2)
    PER = models.CharField(max_length=2)
    CAR = models.CharField(max_length=2)
    VIT = models.CharField(max_length=2)
    FOR = models.CharField(max_length=2)
    LUT = models.CharField(max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




