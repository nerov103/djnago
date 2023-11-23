from django.shortcuts import render
from django.http import HttpResponse
from .models import Tabel
from django.forms import forms
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
#for home views
def home_page(request):
    return render(request, 'home/home.html')


#Login From and from validation Function
def login_or_registration(request):
    if request.method=="POST":
        usern = request.POST['username']
        pasw = request.POST['password']
        
        # User Submit None From
        if not usern or not pasw:
            messages.warning(request, 'Requead This Field...')
            return render(request, 'login/login-or.html')
        
        #User Alrady exisit
        if Tabel.objects.filter(username=usern).exists():
            messages.error(request, 'User is Exists!!')
            return render(request, 'login/login-or.html')
        
        #save in database in user data
        user_data = Tabel(username=usern, password=pasw)
        user_data.save()
        messages.add_message(request, messages.SUCCESS, 'Login Successfully!')
        return render(request, 'login/login-or.html')
    
    else:
        return render(request, 'login/login-or.html')




#User data see in User
def user_data_see(request):
    see_data = UserChangeForm(request.POST, instance=request.user)
    return render(request, 'home/user-data.html', {'us_data':see_data})
