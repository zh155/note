from rest_framework import serializers

from data_cascade import models


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('name', 'price')
