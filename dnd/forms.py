# forms.py
from django import forms
from .models import Race, DndClass, Charbuild

class CharacterForm(forms.ModelForm):
    submit_action = forms.CharField(widget=forms.HiddenInput, initial='submit')
    race = forms.ModelChoiceField(queryset=Race.objects.all(), empty_label='---', required=False)
    classes = forms.ModelChoiceField(queryset=DndClass.objects.all(), empty_label='---', required=False)
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter Character Name'}), required=False)
    age = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter Character Age'}), required=False)
    backstory = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Write Character Backstory'}), required=False)

    class Meta:
        model = Charbuild
        fields = ['name', 'age', 'race', 'classes', 'backstory']