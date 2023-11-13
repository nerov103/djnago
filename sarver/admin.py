from django.contrib import admin
from .models import table

#Create Your Own admin class
@admin.register(table)
class tableAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')



