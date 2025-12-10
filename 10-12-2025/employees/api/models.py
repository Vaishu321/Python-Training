# Create your models here.
from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.name