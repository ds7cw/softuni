from django.db import models

from django.core.validators import MinLengthValidator

from exam_prep_01.accounts.validators import username_char_validation


# Create your models here.
class Profile(models.Model):

    username = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2),
            username_char_validation,
        ],
    )

    email = models.EmailField(blank=False, null=False)

    age = models.PositiveIntegerField(blank=True, null=True) 

    def __str__(self) -> str:
        return self.username