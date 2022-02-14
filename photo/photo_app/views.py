from django.shortcuts import render
from .models import PhotoModel
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


class PhotoUpload(SuccessMessageMixin, CreateView):

    model = PhotoModel
    fields = ['photo', 'description']
    template_name = 'photo_app/photo-upload.html'
    success_url = '/upload_photo/'
    success_message = 'Picture added successfully!'
    error_message = 'Wystąpił błąd. Spróbuj ponownie.'

