
from django import forms
from .models import userdata

class myfm(forms.ModelForm):
    class Meta:
        model = userdata
        fields = ['username', 'email', 'password']

