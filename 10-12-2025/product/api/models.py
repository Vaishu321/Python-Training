# Create your models here.
from django.db import models


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name