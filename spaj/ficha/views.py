from django.shortcuts import render, redirect
from django.views.generic import ListView
from.models import fichas
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login/')
def ficha_register(requeset):
    return render(requeset, 'fichas-register.html')

@login_required(login_url='login/')
def set_ficha(requeset):
    LVL = requeset.POST.get('LVL')
    print(LVL)
    CAR = requeset.POST.get('CAR')
    print(CAR)
    return redirect('/')