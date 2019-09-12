from django.shortcuts import render
from django.views.generic import ListView
from polls.models import Question

class QuestionList(ListView):
  model = Question