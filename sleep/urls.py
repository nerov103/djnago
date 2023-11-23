from django.urls import path
from sleep import views

#create a function
urlpatterns = [
    path('', views.power),
    
]
