from django.urls import path
from.import views

urlpatterns = [
    path('', views.PollsListViews.as_view(), name='polls')
]
