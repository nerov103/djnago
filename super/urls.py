from django.urls import path
from .import views


urlpatterns = [
    path('registration/', views.registration),
    path('post', views.submit),
    path('user/', views.userr),
    path('sub/', views.dan),
    

]

