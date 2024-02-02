# Generated by Django 5.0.1 on 2024-02-02 16:56

import petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='pet_photos/', validators=[petstagram.photos.validators.validate_image_size_below_5mb]),
        ),
    ]
