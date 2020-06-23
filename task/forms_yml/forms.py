from django import forms
from .models import Tyre, Vendor

class TyreForm(forms.ModelForm):

    class Meta:
        model = Tyre
        fields = ('model', 'price')

class VendorForm(forms.ModelForm):

    class Meta:
        model = Vendor
        fields = ('vendor',)

