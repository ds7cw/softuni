from django import forms
from .models import Pet


class PetBaseForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo',]
        labels = {
            'name': 'Pet name',
            'personal_photo': 'Link to image',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Pet name',},
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                }, 
            ),
            'personal_photo': forms.URLInput(
                attrs={'placeholder': 'Link to image',},
            ),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs['disabled'] = 'disabled'
        # self.fields['date_of_birth'].widget.attrs['readonly'] = 'readonly'


class PetDeleteForm(PetBaseForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
