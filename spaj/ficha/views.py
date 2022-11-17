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
from aventura.models import aventuras
from .forms import fichas
from django.core.paginator import Paginator

@login_required(login_url='login/')
def ficha_register(requeset):
    return render(requeset, 'fichas-register.html')
@login_required(login_url='login/')
def set_ficha(requeset):
    if (requeset.method == 'GET'):
        form = fichas()
        context = { 'form': form

        }
        return render(requeset, 'fichas-register.html', context = form)

    if(requeset.method == 'POST'):

        form = fichas(requeset.POST)

        if (form.is_valid()):

            return redirect('/')
        else:
            form = fichas()







@login_required(login_url='login/')
def get_ficha(requeset):
    return render(requeset,'fichas.html')


def equipamentos(requeset):
    id_ficha = requeset.id_ficha
    equipamento = requeset.equipamento
    possuir = possuir_equipamento(id_equi_id=equipamento, id_ficha_id=id_ficha)



# q = aventuras.objects.all()
# x = 1
# for objects in q:
#   e = aventuras.objects.get(id=x)
#   print(e.id, '\n', e.nomeAventura)
#   x = x+1
