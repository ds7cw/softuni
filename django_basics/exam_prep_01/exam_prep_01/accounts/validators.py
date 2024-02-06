import re
from django.core.exceptions import ValidationError


def username_char_validation(value):
    if not re.match(r'^[A-Za-z0-9_]+$', value):
        raise ValidationError(
            'Ensure this value contains only letters, numbers, and underscore.'
        )
