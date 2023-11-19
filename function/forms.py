from django import forms


#Create Forms
class registration_from(forms.Form):
    username = forms.CharField(max_length=100, label='Enter Your Name')
    email = forms.EmailField(label='Enter Email')
    password = forms.IntegerField(label='Enter Password')
    re_password = forms.IntegerField(label='Enter Re_Password')

    
