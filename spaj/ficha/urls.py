from django.urls import path
from django.views.generic import TemplateView
from.import views

urlpatterns = [
    path('fichas', views.get_ficha),
    path('create/', views.fichas),
    path('create/submit', views.set_ficha)
]