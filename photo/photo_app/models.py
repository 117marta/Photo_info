from django.db import models


class PhotoModel(models.Model):
    photo = models.ImageField(upload_to='img/', blank=True, verbose_name='Choose a photo')
    description = models.TextField(verbose_name='Photo comment')
    name = models.CharField(max_length=50, null=True)
    latitude = models.FloatField(null=True, max_length=100)
    longitude = models.FloatField(null=True, max_length=100)
    altitude = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    date_taken = models.CharField(max_length=50, null=True)
    width = models.SmallIntegerField(null=True)
    height = models.SmallIntegerField(null=True)
    camera_name = models.CharField(max_length=100, null=True)
    camera_model = models.CharField(max_length=100, null=True)
