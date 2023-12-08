# forms.py
from django import forms
from .models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['race', 'dnd_class', 'backstory']