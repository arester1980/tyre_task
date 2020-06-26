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


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()