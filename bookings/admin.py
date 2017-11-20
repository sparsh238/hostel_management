from django.contrib import admin
from django.db import models
from .models import booking

@admin.register(booking)
class UploadAdmin(admin.ModelAdmin):
    pass

