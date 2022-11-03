from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import fichas, equipamentos, pericias, possuir_equipamento
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.db.models import Q


class Ficha:
    @login_required(login_url='login/')
    def ficha_register(requeset):
        return render(requeset, 'fichas-register.html')

    @login_required(login_url='login/')
    def set_ficha(requeset):
        LVL = int(requeset.POST.get('LVL'))
        CAR = int(requeset.POST.get('CAR'))
        AGL = int(requeset.POST.get('AGL'))
        DES = int(requeset.POST.get('DES'))
        CTF = int(requeset.POST.get('CTF'))
        SAB = int(requeset.POST.get('SAB'))
        PER = int(requeset.POST.get('PER'))
        CON = int(requeset.POST.get('CON'))
        LUT = (AGL + DES) / 2
        nomep = requeset.POST.get('nomep')
        hta = requeset.POST.get('hta')
        user = requeset.user.id
        aventura = int(requeset.POST.get('aventura'))
        equi = equipamentos.objects.all()
        x = 1
        for objects in equi:
            e = equipamentos.objects.get(id=x)
            print(e.id,'/n',e.nome_equi)
            x = x+1
            pass
        requeset.equipamento = 1
        ficha = fichas.objects.create(Level=LVL, Carisma=CAR, Agilidade=AGL, Vitalidade=CTF, Destreza=DES, ConstFisica=CTF, Sabedoria=SAB, Percepção=PER, Conhecimento=CON,
                                  nomePersonagem=nomep, historiaPersonagem=hta, Luta=LUT, Força=CTF, id_aventura_id = aventura )

        requeset.id_ficha = ficha.id
        equipamento = equipamentos.objects.all()
        print(equipamento)
        print(requeset.possuir_equipamento)
        return redirect('/')

class Equipamentos:
    def equipamentos(requeset):
        id_ficha = requeset.id_ficha
        equipamento = requeset.equipamento
        possuir = possuir_equipamento(id_equi_id = equipamento, id_ficha_id = id_ficha)
