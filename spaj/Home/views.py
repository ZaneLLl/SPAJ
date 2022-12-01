from django.shortcuts import render, redirect
from django.views.generic import ListView
from.models import Post
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q


def register_user(request):
    print(request.user)
    return render(request, 'cadastrar.html')

def submit_user(request):
    if request.POST:
        n_user = request.POST.get('username')
        e_user = request.POST.get('email')
        s_user = request.POST.get('password')
        q = User.objects.filter(username=n_user)
        if len(q)>0:
            messages.error(request, 'Usuário  já cadastrado')
            return render(request, 'cadastrar.html')
        else:
            user = User.objects.create_user(n_user, e_user, s_user)
            user.save()
    return redirect('http://127.0.0.1:8000/login/')


def home(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/home/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/home/')
        else:
            messages.error(request, 'Usuário  ou senha invalidos, tente novame.')
    return redirect('http://127.0.0.1:8000/login/')
