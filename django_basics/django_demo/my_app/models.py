from django.db import models

# Create your models here.
class Player(models.Model):

    TEAM_CHOICES = (
        ('BOS', 'BOS'),
        ('MIA', 'MIA'),
        ('ORL', 'ORL'),
        ('CHI', 'CHI'),
        ('MIL', 'MIL'),
        ('PHI', 'PHI'),
        ('NYK', 'NYK'),
        ('LAL', 'LAL'),
        ('PHO', 'PHO'),
        ('GSW', 'GSW'),
        ('DEN', 'DEN'),
        ('SAC', 'SAC'),
        ('MIN', 'MIN'),
        ('DAL', 'DAL'),
        ('NOP', 'NOP'),
    )

    POSITION_CHOICES = (
        ('G', 'G'),
        ('F', 'F'),
        ('C', 'C'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    team = models.CharField(max_length=50, choices=TEAM_CHOICES)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    ppg = models.DecimalField(max_digits=4, decimal_places=2)
    rpg = models.DecimalField(max_digits=4, decimal_places=2)
    apg = models.DecimalField(max_digits=4, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}' 
    