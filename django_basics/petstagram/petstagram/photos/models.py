from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_image_size_below_5mb

# Create your models here.
class Photo(models.Model):

    photo = models.ImageField(
        upload_to='pet_photos/',
        blank=False,
        null=False,
        validators=[
            validate_image_size_below_5mb,
        ]
    )
    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10),
        ],
        blank = True,
        null = True,
    )
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)
