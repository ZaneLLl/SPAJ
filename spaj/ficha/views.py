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
from .forms import NovaFicha
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect

@login_required(login_url='login/')
def set_ficha (request):
    if request.method == 'GET':
        form = NovaFicha()
        context = {
            'form': form
        }
        return render(request,'fichas-register.html', context=context)
    else:
        form = NovaFicha(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            Level = int(request.POST.get('levelhtml'))
            print(Level)
            Sabedoria = int(request.POST.get('sabedoriahtml'))
            print(Sabedoria)
            Conhecimento = int(request.POST.get('conhecimentohtml'))
            print(Conhecimento)
            Agilidade = int(request.POST.get('agilidadehtml'))
            print(Agilidade)
            Destreza = int(request.POST.get('destrezahtml'))
            print(Destreza)
            ConstFisica = int(request.POST.get('constfisicahtml'))
            print(ConstFisica)
            Percepção = int(request.POST.get('percepcaohtml'))
            print(Percepção)
            Carisma = int(request.POST.get('carismahtml'))
            print(Carisma)


            novaFicha = fichas.objects.create(
            nomePersonagem = form.cleaned_data.get('nomePersonagem'),
            historiaPersonagem = form.cleaned_data.get('historiaPersonagem'),
            id_aventura = form.cleaned_data.get('id_aventura'),
            Level = Level,
            Sabedoria = Sabedoria,
            Agilidade = Agilidade,
            Conhecimento = Conhecimento,
            Destreza = Destreza,
            ConstFisica =  ConstFisica,
            Percepção = Percepção,
            Carisma = Carisma
            )
            novaFicha.save()

            return redirect('/')




#@login_required('http://127.0.0.1:8000/login/')
#def get_ficha(request):
    #return render(request, 'fichas.html')


#def equipamentos(request):
    #id_ficha = request.id_ficha
    #equipamento = request.equipamento
    #possuir = possuir_equipamento(id_equi_id=equipamento, id_ficha_id=id_ficha)



# q = aventuras.objects.all()
# x = 1
# for objects in q:
#   e = aventuras.objects.get(id=x)
#   print(e.id, '\n', e.nomeAventura)
#   x = x+1
