from django.db import models
from django.core.validators import MaxValueValidator


class Hero(models.Model):
    alias = models.CharField(default='Hero', max_length=40)
    name = models.CharField(default='Alice Brown', max_length=40)
    description = models.TextField(default='Brave Hero', max_length=400)

    strength = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])
    intelligence = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])
    magic = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])

    public_recognition = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])

    won_battles = models.PositiveIntegerField(default=0)
    lost_battles = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Hero({self.alias})'
