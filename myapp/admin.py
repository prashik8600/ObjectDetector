from django.contrib import admin
from .models import img

@admin.register(img)
class AdminImage(admin.ModelAdmin):
    list_display=['id','photo','date','files']
