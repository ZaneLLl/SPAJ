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
            Sabedoria = int(request.POST.get('sabedoriahtml'))
            Conhecimento = int(request.POST.get('conhecimentohtml'))
            Agilidade = int(request.POST.get('agilidadehtml'))
            Destreza = int(request.POST.get('destrezahtml'))
            ConstFisica = int(request.POST.get('constfisicahtml'))
            Percepção = int(request.POST.get('percepcaohtml'))
            Carisma = int(request.POST.get('carismahtml'))
            Vitalidade = int(request.POST.get('vitalidadehtml'))
            Força = int(request.POST.get('forcahtml'))
            Luta = int(request.POST.get('lutahtml'))
            if ((Sabedoria <= 17) and (Conhecimento <= 17) and (Agilidade <= 17) and (Destreza <= 17) and (ConstFisica <= 17) and (Percepção <= 17)
                and (Carisma <= 17) and (Vitalidade == ConstFisica) and (Força == ConstFisica)  and (Luta == Agilidade)):

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
                Carisma = Carisma,
                Vitalidade = Vitalidade,
                Força = Força,
                Luta = Luta,
                )
                novaFicha.save()
            return redirect('/ficha/')




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
