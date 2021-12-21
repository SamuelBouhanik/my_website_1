from django import forms
from .models import Card_model

class Card_model_form(forms.ModelForm):
    class Meta:
        model=Card_model
        exclude = ['user']