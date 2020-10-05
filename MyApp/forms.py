from django import forms
from .models import products

class prodabout(forms.ModelForm):
    class Meta:
        model=products
        fields=['about']