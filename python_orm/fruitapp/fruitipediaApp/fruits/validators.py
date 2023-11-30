from django.core.exceptions import ValidationError


def is_alpha_only(value: str):
    if value.isalpha():
        return value
    raise ValidationError('Fruit name should contain only letters!')
        