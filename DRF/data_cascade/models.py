from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    user = models.ForeignKey(User, related_name='book')
