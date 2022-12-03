from django.urls import path
from.import views

urlpatterns = [
    path('', views.initial) ,
    path('home/', views.home),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('home/logout/', views.logout_user),
    path('cadastrar/', views.register_user),
    path('cadastrar/submit', views.submit_user),
    path('home/introducao', views.introducaoJogo),
    path('home/regras', views.regras),
    path('home/sobreSpaj', views.sobreSpaj)

]



