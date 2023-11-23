from django.urls import path
from interface import views

#Create a url 
urlpatterns = [
    path('', views.home_page, name='re-home'),
    path('login/', views.login_or_registration, name='go-regis'),
    
]

