from django.shortcuts import render, redirect
from django.views.generic import ListView
from.models import Post
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q


def register_user(requeset):
    return render(requeset, 'spaj/cadastrar.html')
@csrf_protect
def submit_user(requeset):
    if requeset.POST:
        n_user = requeset.POST.get('username')
        e_user = requeset.POST.get('email')
        s_user = requeset.POST.get('password')
        q = User.objects.filter(username=n_user)
        if len(q)>0:
            messages.error(requeset, 'Usuário  já cadastrado')
            return redirect('/login/#')
        else:
            user = User.objects .create_user(n_user, e_user, s_user)
            user.save()
    return redirect('http://127.0.0.1:8000/login')



@login_required(login_url='login/')
def home(requeset):
    return render(requeset, 'spaj/home.html')

def logout_user(requeset):
    logout(requeset)
    return redirect('/login')

def login_user(requeset):
    return render(requeset, 'spaj/login.html')


@csrf_protect
def submit_login(requeset):
    if requeset.POST:
        username = requeset.POST.get('username')
        password = requeset.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(requeset, user)
            return redirect('/')
        else:
            messages.error(requeset, 'Usuário  ou senha invalidos, tente novame.')
    return redirect('/login/#')
