from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(max_length=10, strip=True, required=True)
    password = forms.CharField(
        max_length=10, 
        strip=True, 
        required=True,
        widget=forms.PasswordInput(attrs={'input_type':'password', 'class': 'custom_input'})
    )
    