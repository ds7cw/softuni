from django import forms
from exam_prep_01.accounts.models import Profile


class ProfileModelForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email@email.com'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age'
                }
            ),
        }

