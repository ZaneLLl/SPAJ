from django.urls import path
from.import views

urlpatterns = [
    path('fichas', views.get_ficha),
    path('register/', views.ficha_register),
    path('register/submit', views.set_ficha)
]