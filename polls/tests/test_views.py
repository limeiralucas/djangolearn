from django.test import TestCase, Client
from django.urls import reverse
from polls.models import Choice, Question


class TestViews(TestCase):
  def test_question_list_GET(self):
    client = Client()
    
    response = client.get(reverse('question_list'))

    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'polls/question_list.html')