from django import forms
from .models import Computer

class ComputerCreateModelForm(forms.ModelForm):

    class Meta:
        model = Computer
        fields = ['cpu', 'gpu', 'description']