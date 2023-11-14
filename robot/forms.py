from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


#Create Class
class bilding(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

#UserChange from field
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        password = None
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined', 'last_login', 'is_superuser')

        


        