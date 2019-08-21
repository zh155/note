from rest_framework import serializers

from study_serializers.models import Person


# 普通序列化
class PersonSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    height = serializers.IntegerField(default=170)
    weight = serializers.IntegerField(default=65)

    def update(self, instance, validated_data):
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.save()
        return instance

    def create(self, validated_data):
        return Person.objects.create(**validated_data)


# 模型序列化
class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'height', 'weight')
