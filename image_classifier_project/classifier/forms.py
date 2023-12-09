from django import forms

class ClassificationForm(forms.Form):
    image = forms.ImageField()
