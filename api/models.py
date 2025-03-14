from django.db import models


class Driver(models.Model):
    image = models.ImageField()
    name =  models.CharField(max_length=255)
    birth_date = models.DateField()
    team = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'Driver: {self.name} | {self.team}'