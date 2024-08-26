from django.contrib import admin
from .models import pdata,hiraaa
class hi(admin.ModelAdmin):
    list_display = ('patient_name','bed_no','doa')
admin.site.register(pdata,hi)
class hii(admin.ModelAdmin):
    list_display = ('name','age')
admin.site.register(hiraaa,hii)