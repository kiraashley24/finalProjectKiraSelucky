# forms.py
from django import forms
from .models import Race, DndClass, Charbuild

class CharacterForm(forms.ModelForm):
    submit_action = forms.CharField(widget=forms.HiddenInput, initial='submit')
    race = forms.ModelChoiceField(queryset=Race.objects.all(), empty_label='---')
    classes = forms.ModelChoiceField(queryset=DndClass.objects.all(), empty_label='---')
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter Character Name'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Character Age'}))
    backstory = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Write Character Backstory...'}))

    class Meta:
        model = Charbuild
        fields = ['name', 'age', 'race', 'classes', 'backstory']