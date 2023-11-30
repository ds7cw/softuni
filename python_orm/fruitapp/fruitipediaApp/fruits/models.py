from django.db import models
from django.core.validators import MinLengthValidator
from fruits.validators import is_alpha_only

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            is_alpha_only,
        ]
    )

    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name