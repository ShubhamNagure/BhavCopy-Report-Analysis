from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(BhavcopyRec)

@admin.register(BhavcopyRec)
class BhavcopyRecAdmin(admin.ModelAdmin):
    list_filter =('sc_name')
    list_display =('sc_name')

