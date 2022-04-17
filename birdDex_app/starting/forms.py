from django import forms
from django.forms.widgets import HiddenInput
from . import models

class JoinForm(forms.Form):
   image = forms.CharField(widget=forms.Textarea)