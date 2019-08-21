from django.db import models


# Create your models here.

class Person(models.Model):
    height = models.IntegerField()
    weight = models.IntegerField()
