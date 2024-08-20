from django.forms import ModelForm
from .models import *
from django import forms

class ResumeForm(forms.ModelForm):
    class Meta:
        model = resume
        fields='__all__'

class SignupForm(forms.ModelForm):
    class Meta:
        model = login
        fields='__all__'
