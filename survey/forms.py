from django.forms import ModelForm
from django import forms
from accounts.models import CustomUser
from .models import Question
class UserDataForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['age', 'sex', 'weight', 'height', 'allergia', 'habbits']

class QuestionForm(forms.Form):
    userAns = forms.CharField(label='', max_length=50)

    