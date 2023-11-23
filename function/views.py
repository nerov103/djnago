from django.shortcuts import render
from .forms import registration_from

# Create your views here.
def registration(request):
    registration_obj = registration_from()
    return render(request, 'login/registration.html', {'data_regis':registration_obj})


