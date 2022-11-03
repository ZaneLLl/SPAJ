from django.urls import path
from.import views

urlpatterns = [
    path('register/', views.Ficha.ficha_register),
    path('register/submit', views.Ficha.set_ficha)
]