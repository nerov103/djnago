from django.urls import path
from .import views

#create own path
urlpatterns = [
    path('regis/', views.registrations, name='render'),
    path('login/', views.login_from, name='template'),
    path('logout/', views.logout_from, name='logout'),
    path('change/', views.Change_pass, name='passw'),
    path('oldpss/', views.chng_pass_without_old_pass, name='chn'),


]




