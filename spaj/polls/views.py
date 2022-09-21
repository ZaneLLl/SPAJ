from django.shortcuts import render
from django.views.generic import ListView
from.models import Question, Choice

class PollsListViews(ListView):
    model = [Question, Choice]
    template_name = 'spaj/polls.html'

