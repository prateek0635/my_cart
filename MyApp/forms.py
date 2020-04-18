from django import forms
from .models import *

class prodimg(forms.ModelForm):
    class Meta:
        model=shop
        fiels=['shop_img']