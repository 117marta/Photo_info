from django.shortcuts import render, HttpResponse
from .models import PhotoModel
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from PIL import Image
import piexif
import folium
from branca.element import Figure


class PhotoUploadView(SuccessMessageMixin, CreateView):

    model = PhotoModel
    fields = ['photo', 'description']
    template_name = 'photo_app/photo-upload.html'
    error_message = 'Error occurred. Try again.'

    def get_success_url(self):
        return f'/upload_photo/{self.object.pk}'


class PhotoInfoView(View):

    def get(self, request, photo_id):
        img = PhotoModel.objects.get(pk=photo_id)

        if img.photo:
            img_opened = Image.open(img.photo.path)
            try:
                # Returns exif data as a dictionary with the following keys unless its value does not exist in the file:
                # “0th”, “Exif”, “GPS”, “Interop”, “1st”, and “thumbnail”.
                exif_dict = piexif.load(img_opened.info['exif'])
                lat = exif_dict['GPS'][piexif.GPSIFD.GPSLatitude]
                lat_ref = exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef].decode('UTF-8')
                lon = exif_dict['GPS'][piexif.GPSIFD.GPSLongitude]
                lon_ref = exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef].decode('UTF-8')
                alt = exif_dict['GPS'][piexif.GPSIFD.GPSAltitude]
                height = exif_dict["0th"][257]
                width = exif_dict["0th"][256]
                date = exif_dict['0th'][piexif.ImageIFD.DateTime].decode('UTF-8')
                camera = exif_dict["0th"][271].decode('UTF-8')
                model = exif_dict["0th"][272].decode('UTF-8')
            except KeyError:
                return HttpResponse('No exif data in photo.')

            # Convert DMS (Degrees/Minutes/Seconds) to DD (Decimal Degrees)
            def get_decimal_degrees(value, ref):
                degrees = value[0][0]
                minutes = value[1][0] / 60
                seconds = value[2][0] / value[2][1] / 3600
                result = degrees + minutes + seconds
                if ref == 'S' or ref == 'W':
                    result = -result
                return result

            lat_decimal = get_decimal_degrees(lat, lat_ref)
            lon_decimal = get_decimal_degrees(lon, lon_ref)

            # Map - photo taken
            w = 800
            h = 500
            figure = Figure(width=w, height=h)
            m = folium.Map(
                location=(lat_decimal, lon_decimal),
                width=w,
                height=h,
                zoom_start=14,
                tiles='OpenStreetMap',
            )
            folium.Marker(
                location=[lat_decimal, lon_decimal],
                tooltip='Photo',
                popup=f'{img.description}',
                icon=folium.Icon(color='red', icon_color='yellow', angle=15, prefix='fa fa-camera'),  # Font Awesome 4
            ).add_to(m)
            figure.add_child(m)
            m = m._repr_html_()

            # Save exif data to the database
            img.latitude = lat_decimal
            img.longitude = lon_decimal
            img.altitude = alt[0] / alt[1]
            img.date_taken = date
            img.width = width
            img.height = height
            img.camera_name = camera
            img.camera_model = model
            img.name = f'{img.pk}. {date}'
            img.save()

            # Get geolocation of user
            lat_user = request.COOKIES.get('lat')
            lon_user = request.COOKIES.get('lon')

            # Map - user geolocation
            if lat_user != None and lon_user != None:
                figure_user = Figure(width=w, height=h)
                m_user = folium.Map(
                    location=(lat_user, lon_user),
                    width=w,
                    height=h,
                    zoom_start=14,
                    tiles='OpenStreetMap',
                )
                folium.Marker(
                    location=[lat_user, lon_user],
                    tooltip='You',
                    popup=':)',
                    icon=folium.Icon(color='black', icon_color='pink', angle=0, prefix='fa fa-map-marker'),
                ).add_to(m_user)
                figure_user.add_child(m_user)
                m_user = m_user._repr_html_()
            else:
                m_user = 'Geolocation could not be obtained. Refresh the page.'

            ctx = {
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
                'lat_decimal': lat_decimal,
                'lon_decimal': lon_decimal,
                'm': m,
                'lat_user': lat_user,
                'lon_user': lon_user,
                'm_user': m_user,
            }
            return render(request=request, template_name='photo_app/photo-info.html', context=ctx)
        else:
            return HttpResponse('No photo added!')
