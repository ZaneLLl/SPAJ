from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import fichas
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


@login_required(login_url='login/')
def ficha_register(requeset):
    return render(requeset, 'fichas-register.html')

@login_required(login_url='login/')
def set_ficha(requeset):
    LVL = requeset.POST.get('LVL')
    CAR = requeset.POST.get('CAR')
    AGL = requeset.POST.get('AGL')
    VIT = requeset.POST.get('VIT')
    DES = requeset.POST.get('DES')
    CTF = requeset.POST.get('CTF')
    SAB = requeset.POST.get('SAB')
    PER = requeset.POST.get('PER')
    CON = requeset.POST.get('CON')
    nomep = requeset.POST.get('nomep')
    hta = requeset.POST.get('hta')
    user = requeset.user

    ficha = fichas.objects.create(LVL=LVL, CAR=CAR, AGL=AGL, VIT=VIT, DES=DES, CTF=CTF, SAB=SAB, PER=PER, CON=CON,
                                  nomePersonagem=nomep, historiaPersonagem=hta)

    return redirect('/')

