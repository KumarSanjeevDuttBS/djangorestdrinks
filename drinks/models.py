from django.db import models


class Drink(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    @property
    def __str__(self):
        return f'{self.name} {self.description}'
