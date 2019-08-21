from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=255)


class Address(models.Model):
    addr = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='address')
