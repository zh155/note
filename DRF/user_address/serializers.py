from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user_address import models


class UserSerializer(serializers.ModelSerializer):
    # def create(self, kwargs):
    #     user = models.User
    #     kwargs['password'] = make_password(kwargs['password'])
    #     user = user.objects.create(**kwargs)
    #     return user

    # def create(self, kwargs):
    #     user = models.User()
    #     # kwargs['password'] = make_password(kwargs['password'])
    #     user.name = kwargs['name']
    #     user.password = kwargs['password']
    #     user.save()
    #     return user

    class Meta:
        model = models.User
        fields = ('name', 'password')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ('addr',)
