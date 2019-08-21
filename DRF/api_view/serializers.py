from rest_framework import serializers

from api_view import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'name', 'age')
        # fields ="__all__"

