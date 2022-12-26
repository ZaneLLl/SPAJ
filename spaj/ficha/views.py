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
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
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
            novaFicha.preencher_ficha.add(request.user)

        else:
            form = NovaFicha(request.POST)
            context = {
                        'form': form
            }
            messages.error(request, 'Dados incorretos')
            return render(request, 'ficha-register.html', context=context)

        return redirect('fichas/')

def get_ficha (request, pk):
        ficha = fichas.objects.filter(pk=pk)
        context = {
            'ficha': ficha
        }
        return render(request,'get-ficha.html', context)






@login_required(login_url='http://127.0.0.1:8000/login/')
def set_pericia(request):
        return render(request, 'pericia-register.html')

@csrf_protect
def submit_pericia(request):
    if request.POST:
        nomepericia = request.POST.get('nome_pericia')
        descricaopericia = request.POST.get('Descrição')
        atrib1 = request.POST.get('Atributo1')
        atrib2 = request.POST.get('Atributo2')
        q = pericias.objects.filter(nome_pericia= nomepericia)
        if len(q)>0:
            messages.error(request, 'Pericia  já cadastrada')
            return render(request, 'pericia-register.html')
        else:
            if(atrib1 == atrib2):
                atrib2 = 0

            pericia = pericias.objects.create(
                nome_pericia =  nomepericia,
                descrição_pericia = descricaopericia,
                atrib1 = int(atrib1),
                atrib2 = int(atrib2)
                )
            pericia.save()

            return redirect('/ficha/pericias/')


class fichasListview(ListView):
    model = fichas
    template_name = 'biblioteca-fichas.html'

    def get_queryset(self):
        return fichas.objects.filter(preencher_ficha=self.request.user.id)

class periciasListview(ListView):
    model = pericias
    template_name = 'biblioteca-pericias.html'

class fichasDeletview(DeleteView):
    model = fichas
    template_name = 'ficha-excluir.html'
    success_url = reverse_lazy('ficha')

class periciasDeletview(DeleteView):
    model = pericias
    template_name = 'pericia-excluir.html'
    success_url = reverse_lazy('pericia')



