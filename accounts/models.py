from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    salary = models.IntegerField()
    status = models.BooleanField()
    image = models.ImageField()