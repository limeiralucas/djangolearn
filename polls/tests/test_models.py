from django.test import TestCase
from polls.models import Question

class TestModels(TestCase):
  def setUp(self):
    self.question1 = Question.objects.create(
      question_text='First Question'
    )

  def test_assigned_question_text(self):
    self.assertEquals(self.question1.question_text, 'First Question')