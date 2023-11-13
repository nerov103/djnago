from django.shortcuts import render,HttpResponsePermanentRedirect
from sarver.forms import user
from.models import table
from django.contrib.auth.forms import AuthenticationForm
#Create Your Views File
def views_from(request):
    fom = AuthenticationForm()
    return render(request, 'from/test.html', {'ff': fom})








