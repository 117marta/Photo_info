from django.db import models


class PhotoModel(models.Model):
    photo = models.ImageField(upload_to='img/', blank=True, verbose_name='Choose photo')
    description = models.TextField(verbose_name='Photo comment')
    name = models.CharField(max_length=50, null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    altitude = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    date_taken = models.DateTimeField(null=True)
    width = models.SmallIntegerField(null=True)
    height = models.SmallIntegerField(null=True)
    camera_name = models.CharField(max_length=100, null=True)
    camera_model = models.CharField(max_length=100, null=True)
