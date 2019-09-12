from django.urls import path

from polls.views import QuestionList

urlpatterns = [
  path('question', QuestionList.as_view(), name='question_list')
]