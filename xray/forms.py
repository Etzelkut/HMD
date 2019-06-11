from django import forms

class HeartDesease(forms.Form):
    age = forms.IntegerField()
    sex = forms.BooleanField()
    chest_pain = forms.IntegerField()


class UploadFileForm(forms.Form):
    file = forms.FileField()