from django.contrib import admin
from .models import ImageUploadModel

# Register your models here.

class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('description', 'document', 'uploaded_at')

admin.site.register(ImageUploadModel, ImageUploadAdmin)
