from django.urls import path
from.import views

urlpatterns = [
    path('register/', views.ficha_register),
    path('register/submit', views.set_ficha)


]