from django.db import models

# Create your models here.
class States(models.Model):
    states_name  = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return  self.states_name

class City(models.Model):
    states_name = models.ForeignKey(States, on_delete=models.CASCADE)
    city_name  = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return  self.city_name

