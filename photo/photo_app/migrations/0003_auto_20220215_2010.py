# Generated by Django 3.2.12 on 2022-02-15 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0002_auto_20220215_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photomodel',
            name='latitude',
            field=models.FloatField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='photomodel',
            name='longitude',
            field=models.FloatField(max_length=100, null=True),
        ),
    ]
