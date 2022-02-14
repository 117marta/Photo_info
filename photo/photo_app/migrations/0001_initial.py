# Generated by Django 3.2.12 on 2022-02-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='img/', verbose_name='Choose photo')),
                ('description', models.TextField(verbose_name='Photo comment')),
                ('name', models.CharField(max_length=50, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('altitude', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('date_taken', models.DateTimeField(null=True)),
                ('width', models.SmallIntegerField(null=True)),
                ('height', models.SmallIntegerField(null=True)),
                ('camera_name', models.CharField(max_length=100, null=True)),
                ('camera_model', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]