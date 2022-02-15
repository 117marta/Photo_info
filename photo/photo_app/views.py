import folium as folium
from django.shortcuts import render, HttpResponse
from .models import PhotoModel
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from PIL import Image
import piexif


class PhotoUploadView(SuccessMessageMixin, CreateView):

    model = PhotoModel
    fields = ['photo', 'description']
    template_name = 'photo_app/photo-upload.html'
    success_url = '/upload_photo/'
    success_message = 'Picture added successfully!'
    error_message = 'Wystąpił błąd. Spróbuj ponownie.'

    def get_success_url(self):
        return f'/upload_photo/{self.object.pk}'


class PhotoInfoView(View):

    def get(self, request, photo_id):
        img = PhotoModel.objects.get(pk=photo_id)

        if img.photo:
            img_opened = Image.open(img.photo.path)
            try:
                exif_dict = piexif.load(img_opened.info['exif'])
                lat = exif_dict['GPS'][piexif.GPSIFD.GPSLatitude]
                lat_ref = exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef]
                lon = exif_dict['GPS'][piexif.GPSIFD.GPSLongitude]
                lon_ref = exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef]
                alt = exif_dict['GPS'][piexif.GPSIFD.GPSAltitude]
                height = exif_dict["0th"][257]
                width = exif_dict["0th"][256]
                date = exif_dict['0th'][piexif.ImageIFD.DateTime]
                camera = exif_dict["0th"][271]
                model = exif_dict["0th"][272]
            except KeyError:
                return HttpResponse('No exif data in photo.')

            ctx = {
                'img_opened': img_opened,
                'img': img,
                'lat': lat,
                'lat_ref': lat_ref,
                'lon': lon,
                'lon_ref': lon_ref,
                'alt': alt,
                'width': width,
                'height': height,
                'date': date,
                'camera': camera,
                'model': model,
            }
            return render(request=request, template_name='photo_app/photo-info.html', context=ctx)
        else:
            return HttpResponse('No photo added!')

