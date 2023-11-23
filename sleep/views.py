from django.shortcuts import render
from .models import database
from django.contrib import messages
# Create your views here.
def power(request):
    if request.method=='POST':
        usern = request.POST['username']
        pasw = request.POST['password']
        
        
        #Same program
        if database.objects.filter(username=usern):
            ms = 'Users Already exits!'
            return render(request, 'home/login-fm.html', {'mass': ms})
        else:
            newuser = database.objects.create(username=usern, password=pasw)
            newuser.save()
            succes = 'Login Successfully!'
            # messages.add_message(request, messages.SUCCESS, 'Login Successfull!')
            return render(request, 'home/login-fm.html', {'suc':succes})
    else:
        print('get method!')
        return render(request, 'home/login-fm.html')
    


