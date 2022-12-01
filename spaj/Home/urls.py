from django.urls import path
from.import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('cadastrar/', views.register_user),
    path('cadastrar/submit', views.submit_user)

]


