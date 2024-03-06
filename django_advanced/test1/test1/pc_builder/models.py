from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ComputerComponent(models.Model):

    class Meta:
        abstract = True

    class ManufacturerChoices(models.TextChoices):
        pass

    manufacturer = models.CharField(
        max_length=10,
        choices = ManufacturerChoices.choices,
    )

    model_name = models.CharField(
        max_length=40,
        unique=True,
    )

    core_count = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )


class Processor(ComputerComponent):

    class ManufacturerChoices(models.TextChoices):
        INTEL = 'INTEL', 'Intel'
        AMD = 'AMD', 'AMD'

    p_core_base_clock = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0.1),
        ],
    ) 

    p_core_max_clock = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0.1),
        ],
    )

    def __str__(self) -> str:
        return self.model_name


class GraphicsCard(ComputerComponent):

    class ManufacturerChoices(models.TextChoices):
        INTEL = 'INTEL', 'Intel'
        AMD = 'AMD', 'AMD',
        NVIDIA = 'NVIDIA', 'Nvidia'

    gpu_base_clock = models.SmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(10_000),
            MinValueValidator(1),
        ],
    ) 

    gpu_max_clock = models.SmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(10_000),
            MinValueValidator(1),
        ],
    )

    def __str__(self) -> str:
        return self.model_name


class Computer(models.Model):

    cpu = models.ForeignKey('Processor', on_delete=models.CASCADE,related_name='computers')
    gpu = models.ForeignKey('GraphicsCard', on_delete=models.CASCADE,related_name='computers')
    description = models.TextField(max_length=500, null=True, blank=True)
