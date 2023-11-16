from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from .forms import bilding, CustomUserChangeForm
# Create your views here.


#registeations
def registrations(request):
    if request.method=='POST':
        obj_usercreation_from = bilding(request.POST)
        if obj_usercreation_from.is_valid():
            obj_usercreation_from.save()
            return HttpResponseRedirect('/super/post')
    else:
        obj_usercreation_from = bilding()
    return render(request, 'exple/login.html', {'pass_valie':obj_usercreation_from})



#Login
def login_from(request):
    if request.method=="POST":         
        frm = AuthenticationForm(request=request, data=request.POST)
        if frm.is_valid():
            usern = frm.cleaned_data['username']
            passw = frm.cleaned_data['password']
            user = authenticate(username=usern, password=passw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/robot/sube')
    else:
        print('Get Method!')
        frm = AuthenticationForm()
    return render(request, 'exple/index.html', {'fom':frm})
 


#Login Successfully
def successfully(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            frm = CustomUserChangeForm(request.POST ,instance = request.user)
            if frm.is_valid():
                frm.save()
        else:
            frm = CustomUserChangeForm(instance = request.user)

        return render(request, 'exple/suc.html', {'data_frm': frm})
    else:
        return HttpResponseRedirect('/robot/sube')



#Logout
def logout_from(request):
    logout(request)
    return HttpResponseRedirect('/robot/login')


#Change pass
def Change_pass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            pas = PasswordChangeForm(user=request.user, data=request.POST)
            if pas.is_valid():
                pas.save()
                update_session_auth_hash(request, pas.user)
                return HttpResponseRedirect('/robot/sube')
        else:
            pas = PasswordChangeForm(user=request.user)
        return render(request, 'exple/change.html', {'ch':pas})
    else:
        return HttpResponseRedirect('/robot/login')


#Change pass without old password
def chng_pass_without_old_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            pas_ch = SetPasswordForm(user=request.user, data=request.POST)
            if pas_ch.is_valid():
                pas_ch.save()
                update_session_auth_hash(request, pas_ch.user)
                return HttpResponseRedirect('/robot/sube')
        else:
            pas_ch = SetPasswordForm(user=request.POST)
        return render(request, 'exple/without-pass.html', {'chng':pas_ch})
    else:
        return HttpResponseRedirect('/superr/login')



