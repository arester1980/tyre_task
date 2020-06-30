from django import forms
from .models import Tyre


class TyreForm(forms.ModelForm):
    class Meta:
        model = Tyre
        fields = ['model', 'price']