from django.contrib import admin
from .models import userdata

# Register your models here.
@admin.register(userdata)
class userdataAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']
    