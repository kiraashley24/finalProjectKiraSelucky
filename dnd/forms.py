# forms.py
from django import forms
from .models import Race, DndClass, Charbuild

class CharacterForm(forms.ModelForm):
    race = forms.ModelChoiceField(queryset=Race.objects.all(), label='Race')
    dnd_class = forms.ModelChoiceField(queryset=DndClass.objects.all(), label='Class')
    backstory = forms.CharField(widget=forms.Textarea, label='Backstory')

    class Meta:
        model = Charbuild
        fields = ['name', 'age', 'race', 'dnd_class', 'backstory']
