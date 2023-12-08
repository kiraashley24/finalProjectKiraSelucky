# forms.py
from django import forms
from .models import Race, DndClass, Charbuild

class CharacterForm(forms.ModelForm):
    submit_action = forms.CharField(widget=forms.HiddenInput, initial='submit')

    class Meta:
        model = Charbuild
        fields = ['name', 'age', 'race', 'classes', 'backstory']