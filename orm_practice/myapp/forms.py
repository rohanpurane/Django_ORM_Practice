from django import forms
from .models import *

class WholeSaleShopForm(forms.ModelForm):
    class Meta:
        model = WholeSaleShop
        fields = ('w_name', 'w_qty')

class RetailShopForm(forms.ModelForm):
    class Meta:
        model = RetailShop
        fields = ('r_name', 'r_qty')

