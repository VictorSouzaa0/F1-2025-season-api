from django.db import models


class Driver(models.Model):
    image = models.ImageField('media')
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    tag = models.CharField(max_length=3)
    team = models.CharField(max_length=50)

    def  __str__(self):
        return f'{self.name} | {self.tag}'
    
