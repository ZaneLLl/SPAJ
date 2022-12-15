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
from .forms import NovaFicha, NovaPericia
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect

@login_required(login_url='http://127.0.0.1:8000/login/')
def set_ficha (request):
    if request.method == 'GET':
        form = NovaFicha()
        context = {
            'form': form
        }
        return render(request,'ficha-register.html', context=context)
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
        else:
            form = NovaFicha(request.POST)
            context = {
                        'form': form
            }
            return render(request, 'ficha-register.html', context=context)

        return redirect('fichas/')




@login_required(login_url='http://127.0.0.1:8000/login/')
def set_pericia(request):
    if request.method == 'GET':
        form = NovaPericia()
        context ={
            'form': form
        }
        return render(request, 'pericia-register.html', context=context)
    else:
        form = NovaPericia(request.POST)
        context = {
            'form': form
        }
        return render(request, 'pericia-register.html', context=context)