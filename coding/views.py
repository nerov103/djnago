from django.shortcuts import render, HttpResponse
from .forms import myfm 
from django.contrib import messages
# Make sure to import your form
#create function
def massge(request):
    if request.method == 'POST':
        frm = myfm(request.POST)
        if frm.is_valid():
            frm.save()  # Assuming you have a model associated with this form
            messages.add_message(request, messages.SUCCESS, 'Login Successfully ')
          
    else:
        frm = myfm()
    return render(request, 'login/massge.html', {'ff': frm})

