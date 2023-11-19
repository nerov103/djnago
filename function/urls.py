from django.urls import path
from function import views
#Create Urlpatten
urlpatterns = [
    path('registration/', views.registration),
    
]
