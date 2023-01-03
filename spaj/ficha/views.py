from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import fichas, equipamentos, pericias, aventuras
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.db.models import Q
from .forms import NovaFicha, NovaAventura
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from braces.views import GroupRequiredMixin, LoginRequiredMixin

@login_required(login_url='http://127.0.0.1:8000/login/')
def set_ficha(request):
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
            Level = (request.POST.get('levelhtml'))
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
            pericia = (form.cleaned_data.get('conter_pericia'))
            equipamento = (form.cleaned_data.get('possuir_equipamento'))
            print(Força)
            print(Luta)

            if len(pericia) > Conhecimento:
                form = NovaFicha(request.POST)
                context = {
                    'form': form
                }
                messages.error(request, 'Número de pericias maior que o Conhecimento')
                return render(request, 'ficha-register.html', context=context)

            else:
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
                ListaUser = aventuras.objects.get(nomeAventura = novaFicha.id_aventura)
                print(ListaUser)
                l = ListaUser.jogar_aventura.all()
                print(l)
                if len(l) > 0:

                    form = NovaFicha(request.POST)
                    context = {
                        'form': form
                    }
                    messages.error(request, 'O Usuário já está jogando  a aventura')
                    return render(request, 'ficha-register.html', context=context)
                else:

                    novaFicha.save()
                    novaFicha.preencher_ficha.add(request.user)
                    novaFicha.id_aventura.jogar_aventura.add(request.user.id)

                    contador = 0
                    while contador < len(pericia):
                        q = pericias.objects.get(nome_pericia= pericia[contador])
                        novaFicha.conter_pericia.add(q.id)
                        contador = contador + 1

                    contador2 = 0
                    while contador2 < len(equipamento):
                        print(equipamento[contador2])
                        r = equipamentos.objects.get(nome_equi=equipamento[contador2])
                        print(r)
                        novaFicha.possuir_equipamento.add(r.id)
                        contador2 = contador2 + 1

        else:
            form = NovaFicha(request.POST)
            context = {
                        'form': form
            }
            messages.error(request, 'Dados incorretos')
            return render(request, 'ficha-register.html', context=context)

        return redirect('/ficha/')


@login_required(login_url='http://127.0.0.1:8000/login/')
def get_ficha(request, pk):
        ficha = fichas.objects.filter(pk=pk)
        n = fichas.objects.get(pk=pk)
        pericia = n.conter_pericia.all()
        contador = 0
        while len(pericia) > contador :
            q = n.conter_pericia.get(nome_pericia = pericia[contador])
            contador = contador + 1
            bonus = bonus_pericia(q.id, n.id)

        a = fichas.objects.get(pk = n.id)
        aventura = a.id_aventura
        context = {
            'ficha': ficha, 'pericia': pericia, 'bonus': bonus, 'aventura': aventura
        }
        return render(request, 'get-ficha.html', context)
@login_required(login_url='http://127.0.0.1:8000/login/')
def get_pericia(request, pk):
    pericia = pericias.objects.filter(pk=pk)
    n = pericias.objects.get(pk=pk)
    if n.atrib1 == 1:
        a1 = ('Sabedoria')
    else:
        if n.atrib1 == 2:
            a1 = ('Conhecimento')
        else:
            if n.atrib1 == 3:
               a1 = ('Agilidade')
            else:
                if n.atrib1 == 4:
                    a1 = ('Destreza')
                else:
                    if n.atrib1 == 5:
                        a1 = ('Contituição Fisica')
                    else:
                        if n.atrib1 == 6:
                            a1 = ('Percepção')
                        else:
                            if n.atrib1 == 7:
                                a1 = ('Carisma')
    if n.atrib2 == 1:
        a2 = ('Sabedoria')
    else:
        if n.atrib2 == 2:
            a2 = ('Conhecimento')
        else:
            if n.atrib2 == 3:
               a2 = ('Agilidade')
            else:
                if n.atrib2 == 4:
                    a2 = ('Destreza')
                else:
                    if n.atrib2 == 5:
                        a2 = ('Contituição Fisica')
                    else:
                        if n.atrib2 == 6:
                            a2 = ('Percepção')
                        else:
                            if n.atrib2 == 7:
                                a2 = ('Carisma')
                            else:
                                a2 = 0

    context = {
        'pericia': pericia, 'a1':a1, 'a2':a2
    }
    return render(request, 'get-pericia.html', context)

def bonus_pericia( idPericia, idFicha):
    pericia = pericias.objects.get(pk=idPericia)
    a1 = pericia.atrib1
    a2 = pericia.atrib2

    atributo = fichas.objects.get(pk=idFicha)
    if a1 == 1:
        atributo1 = atributo.Sabedoria
    else:
        if a1 == 2:
            atributo1 = atributo.Conhecimento
        else:
            if a1 == 3:
                atributo1 = atributo.Agilidade
            else:
                if a1 == 4:
                    atributo1 = atributo.Destreza
                else:
                    if a1 == 5:
                        atributo1 = atributo.ConstFisica
                    else:
                        if a1 == 6:
                            atributo1 = atributo.Percepção
                        else:
                            if a1 == 7:
                                atributo1 = atributo.Carisma

    if a2 == 1:
        atributo2 = atributo.Sabedoria
    else:
        if a2 == 2:
            atributo2 = atributo.Conhecimento
        else:
            if a2 == 3:
                atributo2 = atributo.Agilidade
            else:
                if a2 == 4:
                    atributo2 = atributo.Destreza
                else:
                    if a2 == 5:
                        atributo2 = atributo.ConstFisica
                    else:
                        if a2 == 6:
                            atributo2 = atributo.Percepção
                        else:
                            if a2 == 7:
                                atributo2 = atributo.Carisma
                            else:
                                atributo2 = atributo1

    bonus = (int(atributo1)+int(atributo2))/2

    return bonus


@login_required(login_url='http://127.0.0.1:8000/login/')
def set_pericia(request):
        if request.user.is_superuser == 1:
            return render(request, 'pericia-register.html')
        else:
                messages.error(request, 'Usuario sem permissão')
                return redirect('http://127.0.0.1:8000/')

@csrf_protect
def submit_pericia(request):
    if request.POST:
        nomepericia = request.POST.get('nome_pericia')
        descricaopericia = request.POST.get('Descrição')
        atrib1 = request.POST.get('Atributo1')
        atrib2 = request.POST.get('Atributo2')
        combate = request.POST.get('combate')
        q = pericias.objects.filter(nome_pericia= nomepericia)
        if len(q)>0:
            messages.error(request, 'Pericia  já cadastrada')
            return render(request, 'pericia-register.html')
        else:
            if atrib2 == atrib1:
                atrib2 = 0

            pericia = pericias.objects.create(
                nome_pericia =  nomepericia,
                descrição_pericia = descricaopericia,
                atrib1 = int(atrib1),
                atrib2 = int(atrib2),
                combate = bool(combate)
                )
            pericia.save()

            return redirect('/ficha/pericia/')



class fichasListview(LoginRequiredMixin, ListView):
    login_url = ('http://127.0.0.1:8000/login/')
    model = fichas
    template_name = 'biblioteca-fichas.html'

    def get_queryset(self):
        return fichas.objects.filter(preencher_ficha=self.request.user.id)


class periciasListview(LoginRequiredMixin, ListView):
    login_url = ('http://127.0.0.1:8000/login/')
    model = pericias
    template_name = 'biblioteca-pericias.html'


class fichasDeletview(LoginRequiredMixin, DeleteView):
    login_url = ('http://127.0.0.1:8000/login/')
    model = fichas
    template_name = 'ficha-excluir.html'
    success_url = reverse_lazy('ficha')


class periciasDeletview(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = ('http://127.0.0.1:8000/login/')
    group_required = u'Mestre'
    model = pericias
    template_name = 'pericia-excluir.html'
    success_url = reverse_lazy('pericia')

def setAventura(request):
    if request.method == 'GET':
        form = NovaAventura()
        context = {
            'form': form
        }
        return render (request, 'aventura-register.html', context = context)

    else:
        form = NovaAventura(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            novaAventura = aventuras.objects.create(

                nomeAventura = form.cleaned_data.get('nomeAventura'),
                guia_de_ambiente = form.cleaned_data.get('guia_de_ambiente'),
                historia_aventura =  form.cleaned_data.get('historia_aventura')
                )

            novaAventura.save()
            return redirect('aventuras/')

        else:
            form = NovaAventura(request.POST)
            context = {
                    'form': form
            }
            messages.error(request, 'Dados incorretos')
            return render(request, 'aventura-register.html', context=context)

class aventurasListview(ListView):
    model = aventuras
    template_name = 'biblioteca-aventuras.html'

    def get_context_data(self, **kwargs):
        context = super(aventurasListview, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
class aventurasDeletview(GroupRequiredMixin, DeleteView):
    login_url = ('http://127.0.0.1:8000/login/')
    model = aventuras
    group_required = u'Mestre'
    template_name = 'aventura-excluir.html'
    success_url = reverse_lazy('aventuras')


def getAventura(request, pk):
    aventura = aventuras.objects.filter(pk=pk)
    context={
        'aventura': aventura
    }
    return render(request, 'get-aventuras.html', context=context)
