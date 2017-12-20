from  django import forms
from . import models

class CheckoutContactForm(forms.Form):
    name=forms.CharField(required=True)
    phone=forms.CharField(required=True)
    adress = forms.CharField(required=True)
    email=forms.EmailField(required=True)
