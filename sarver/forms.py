from django.core.exceptions import ValidationError
from django import forms
from django.core import validators

#Creating a form field
class user(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput)
    



#forms validation function
    def clean_password(self):
        password_valadation = self.cleaned_data['password']
        if len(password_valadation)<5:
            raise ValidationError(("This password is too short. It must contain at least 5 characters."), code="invalid")
        return password_valadation
 

