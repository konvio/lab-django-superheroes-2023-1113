from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=60)
    power = models.IntegerField(default=0)

    def __str__(self):
        return self.name
