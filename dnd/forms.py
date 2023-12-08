from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Race, DndClass, Charbuild

class CharacterForm(forms.ModelForm):
    submit_action = forms.CharField(widget=forms.HiddenInput, initial='submit')
    race = forms.ModelChoiceField(queryset=Race.objects.all(), empty_label='---')
    classes = forms.ModelChoiceField(queryset=DndClass.objects.all(), empty_label='---')
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter Character Name'}))
    age = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Character Age'}),
        validators=[
            MinValueValidator(1, message='Your minimum age must be 1.'),
            MaxValueValidator(500, message='Your maximum age must be 500.')
        ]
    )
    backstory = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Write Character Backstory...'}))

    class Meta:
        model = Charbuild
        fields = ['name', 'age', 'race', 'classes', 'backstory']
