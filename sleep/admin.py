from django.contrib import admin
from .models import database
# Register your models here.
@admin.register(database)
class databaseAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']
    