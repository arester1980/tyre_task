from django import forms
from django.forms import TextInput, NumberInput
from .models import Tyre, Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor']
        widgets = {
            'vendor': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Vendor'
        })
        }

class TyreForm(forms.ModelForm):
    class Meta:
        model = Tyre
        fields = ['vendor', 'model', 'price']
        widgets = {
            'vendor': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Vendor'
            }),
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Model'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price'
                }),
        }