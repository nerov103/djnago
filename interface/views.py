from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
#for home views
def home_page(request):
    return render(request, 'home/home.html')


#for login template
def login_or_registration(request):
    if request.method=='POST':
        usern = request.POST['username']
        pasw = request.POST['password']
        print(usern)
        print(pasw)
        print('post method')
        
    else:
        print('get method')
        return render(request, 'login/login-or.html')
    
    return render(request, 'login/login-or.html')



