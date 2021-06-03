from django import forms
from .models import img

class ImageForm(forms.ModelForm):
    class Meta:
        model=img
        fields='__all__'
        labels={'photo':'Uplaod Image','files':'Upload XML'}