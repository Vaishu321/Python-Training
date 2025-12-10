# Create your models here.
from django.db import models


class Vehicle(models.Model):
    objects = None
    number_plate = models.CharField(max_length=50)
    vehicle_type= models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.number_plate
