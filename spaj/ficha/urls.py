from django.urls import path
from django.views.generic import TemplateView
from.import views

urlpatterns = [
    path('', views.fichasListview.as_view(), name = 'ficha'),
    path('create/', views.set_ficha),
    path('create/submit', views.set_ficha),
    path('create/pericia/', views.set_pericia),
    path('create/pericia/submit', views.submit_pericia),
    path('pericia/', views.periciasListview.as_view(), name = 'pericia'),
    path('delete/<int:pk>/', views.fichasDeletview.as_view()),
    path('pericia/delete/<int:pk>/', views.periciasDeletview.as_view()),
    path('get-ficha/<int:pk>/', views.get_ficha),
    path('pericia/get-pericia/<int:pk>/', views.get_pericia),
    path('aventuras/register/', views.setAventura),
    path('aventuras/register/submit', views.setAventura),
    path('aventuras/', views.aventurasListview.as_view(), name = 'aventuras'),
    path('aventuras/get-aventura/<int:pk>/', views.getAventura),
    path('aventuras/delete/<int:pk>/', views.aventurasDeletview.as_view()),

]