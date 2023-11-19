from django.urls import path
from interface import views

#Create a url 
urlpatterns = [
    path('', views.home_page),
    path('login/', views.login_or_registration),
    
]

