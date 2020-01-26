from django import forms
from django.forms import ModelForm
from .models import Student


class MyForm(forms.Form):
    name = forms.CharField(max_length=60)


class registerstudent(ModelForm):
    class Meta:
        model =Student
        fields = '__all__'
