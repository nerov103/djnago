from django.urls import path
from coding import views

#Create a url
urlpatterns = [
    path('', views.massge),
]
