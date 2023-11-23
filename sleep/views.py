from django.shortcuts import render
from .models import database
from django.contrib import messages
# Create your views here.
def power(request):
    if request.method=='POST':
        usern = request.POST['username']
        pasw = request.POST['password']
        
        
        #from validate
        if not usern or not pasw:
            messages.error(request, 'Requead Uername and Password!!')
            return render(request, 'home/login-fm.html')

        #Same program
        if database.objects.filter(username=usern).exists():
            ms = 'Users Already exits!'
            return render(request, 'home/login-fm.html', {'mass': ms})
        else:
            newuser = database.objects.create(username=usern, password=pasw)
            newuser.save()
            messages.success(request, 'Login Successfully!')
            return render(request, 'home/login-fm.html')
    else:
        print('get method!')
        return render(request, 'home/login-fm.html')
    


