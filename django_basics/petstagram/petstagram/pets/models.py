from django.db import models
from django.utils.text import slugify

# Create your models here.

class Pet(models.Model):

    name = models.CharField(max_length=30, null=False, blank=False)
    personal_photo = models.URLField()
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.pk}')
        
        return super().save(*args, **kwargs)
