from django import forms
from .models import Player


class PlayerModelForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'
        widgets = {
            'dob': forms.SelectDateWidget(
                years=[y for y in range(1980, 2009)],
            ),
        }
        labels = {
            'dob': 'Year of Birth',
            'ppg': 'Points Per Game',
            'rpg': 'Rebounds Per Game',
            'apg': 'Assists Per Game',
        }
