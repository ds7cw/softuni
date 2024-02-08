from django import forms
from .models import Album


class AlbumModelForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'genre', 'description', 'image_url', 'price']
        # Alternative to the above
        # fields = '__all__'
        # exclude = ['owner']
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name...',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist Name...',
                }
            ),
            'genre': forms.Select(
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description...',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL...',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price...',
                }
            ),
        }

        labels = {
            'album_name': 'Album Name',
            'image_url': 'Image URL',
        }