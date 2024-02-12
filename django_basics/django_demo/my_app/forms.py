from django import forms
from .models import Player


class PlayerModelForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(
                attrs={
                    'type': 'date',
                },
            ),
        }
        labels = {
            'dob': 'Year of Birth',
            'ppg': 'Points Per Game',
            'rpg': 'Rebounds Per Game',
            'apg': 'Assists Per Game',
        }


class DeletePlayerModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            # self.fields[field_name].widget.attrs['readonly'] = 'readonly'
            self.fields[field_name].widget.attrs['disabled'] = 'disabled'
        
    class Meta:
        model = Player
        fields = '__all__'

