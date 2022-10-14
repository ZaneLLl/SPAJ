from django.urls import path
from.import views

urlpatterns = [
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('', views.home),
    path('logout/', views.login_user),
    path('cadastrar/', views.register_user),
    path('cadastrar/submit', views.submit_user),
    path ('logout', views.logout_user)
]
