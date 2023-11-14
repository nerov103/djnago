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





