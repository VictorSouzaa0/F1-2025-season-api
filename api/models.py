from django.db import models
class Driver(models.Model):
    image = models.ImageField('/drivers/')
    name =  models.CharField(max_length=255, primary_key=True)
    birth_date = models.DateField()
    team = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'Driver: {self.name} | {self.team}'
    
class Legend(models.Model):
    image = models.ImageField('/legends/')
    name = models.CharField(max_length=255, primary_key=True)
    birth_date = models.DateField()
    country = models.CharField(max_length=100)
    championships = models.IntegerField()
    teams = models.TextField()

    def __str__(self):
        return f"Driver: {self.name} | {self.country}"