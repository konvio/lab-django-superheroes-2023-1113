from django.db import models
from django.core.validators import MaxValueValidator


class Villain(models.Model):
    alias = models.CharField(default='Villain', max_length=40)
    name = models.CharField(default='John Doe', max_length=40)
    description = models.TextField(default='Smart villain', max_length=400)

    strength = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])
    intelligence = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])
    magic = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])

    criminal_network_power = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])

    won_battles = models.PositiveIntegerField(default=0)
    lost_battles = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Villain({self.alias})'
