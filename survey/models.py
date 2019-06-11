from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

class Question(models.Model):
  question = models.CharField(max_length=200)
  first = models.BooleanField(default=False)
  def __str__(self):
    return str(self.question)

class Answer(models.Model):
  question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True, related_name='curr_question')
  answer = models.CharField(max_length=50)
  diagnosis = models.CharField(max_length=100, blank=True, null=True)
  next_question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True, related_name='next_question', blank=True)
  def __str__(self):
    return str(self.question) + " ans:" + str(self.answer)
