from django.db import models
from django.core.validators import MinValueValidator
from exam_prep_01.accounts.models import Profile


# Create your models here.
class Album(models.Model):

    GENRE_CHOICES = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    )

    album_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        unique=True,
    )
    
    artist = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )
    
    genre = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=GENRE_CHOICES,
    )

    description = models.TextField(null=True, blank=True)
    
    image_url = models.URLField(blank=False, null=False)
    
    price = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ],
        null=False,
        blank=False,
    )
    
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.album_name
