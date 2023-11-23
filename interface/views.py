from django.shortcuts import render
from django.http import HttpResponse
from .models import Tabel
from django.forms import forms
# Create your views here.
#for home views
def home_page(request):
    return render(request, 'home/home.html')


#for login template
def login_or_registration(request):
    if request.method=='POST':
        if request.POST == None:
            raise forms.ValidationError(params={"value": "42"})
            return render(request, 'login/login-or.html',{'err':value})
        else:
            usrn = request.POST.get('username')
            parw = request.POST.get('password')
            user_data = Tabel(username=usrn ,password=parw)
            user_data.save()
        
    else:
        print('Get Method Run!')
        return render(request, 'login/login-or.html')
    return render(request, 'login/login-or.html')





