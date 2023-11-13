from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


#Create Your ' Function




# Create your views here.
def registration(request):
    return render(request, 'exple/registration.html')

def submit(request):
    return render(request, 'exple/submit.html')

def dan(request):
    return render(request, 'exple/suc.html')


 
def userr(request):
    if request.method =='POST':
        fome = UserCreationForm(request.POST)
        if fome.is_valid():
            fome.save()
    else:
        fome = UserCreationForm()
    return render(request, 'exple/render.html', {'fome': fome})





