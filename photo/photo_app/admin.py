from django.contrib import admin
from .models import PhotoModel


# admin.site.register(PhotoModel)

@admin.register(PhotoModel)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'date_taken', 'latitude', 'longitude']
    exclude = ['latitude', 'longitude', 'altitude']  # non-editable fields
