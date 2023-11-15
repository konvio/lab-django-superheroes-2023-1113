from django.db import models


class Villain(models.Model):
    name = models.CharField(max_length=60)
    power = models.IntegerField(default=0)

    def __str__(self):
        return self.name
