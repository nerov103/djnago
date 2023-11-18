from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


#Create Your ' Function




# Create your views here.
def registration(request):
    return render(request, 'exple/registration.html')



def submit(request):
    return render(request, 'exple/submit.html')


# # # Successfully Login 
# def dan(request):
#     ff = UserChangeForm()
#     return render(request, 'exple/suc.html', {'chng_from':ff})




 
def userr(request):
    if request.method =='POST':
        fome = UserCreationForm(request.POST)
        if fome.is_valid():
            fome.save()
    else:
        fome = UserCreationForm()
    return render(request, 'exple/render.html', {'fome': fome})


#Creating a function in django
def data_pass(request):
    data = {
        'user' : 'Nerov Ahmead',
        'eml' : 'email@gamil.com'
    }
    return render(request, 'test/index.html', {'data': data})
