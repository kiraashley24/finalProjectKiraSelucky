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
        validators=[MinValueValidator(1, message='You have to be between 1 and 500 years old'), MaxValueValidator(500)]
    )
    backstory = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Write Character Backstory...'}))

    class Meta:
        model = Charbuild
        fields = ['name', 'age', 'race', 'classes', 'backstory']

    def clean(self):
        cleaned_data = super().clean()
        submit_action = cleaned_data.get('submit_action')

        # Check if 'Create Character' button is pressed
        if submit_action == 'Create Character':
            # Validate that all fields are filled out
            for field_name, field_value in cleaned_data.items():
                if not field_value:
                    self.add_error(field_name, f'This field is required.')

        return cleaned_data
