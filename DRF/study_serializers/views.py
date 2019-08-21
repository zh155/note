from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import render

# Create your views here.
from django.views import View

from study_serializers import serializers, models


class PersonView(View):

    def get(self, response):

        # 查询一条数据
        # person = models.Person.objects.all().first()

        # person_serializer = serializers.PersonSerializers(self.person)
        #
        # return JsonResponse(person_serializer.data)

        # 查询多条数据
        people_serializer = serializers.PersonSerializers(models.Person.objects.all(), many=True)
        print(people_serializer.data)
        return JsonResponse({'data': people_serializer.data})

    def patch(self, response):
        serializer = serializers.PersonSerializers(data=dict(height=180, weight=75))
        if serializer.is_valid():
            serializer.save()
            res_data = {
                'status': 201,
                'msg': 'ok',
                'data': serializer.data,
            }
            return JsonResponse(res_data)
        else:
            return JsonResponse(serializer.errors)


class PersonModel(View):
    def get(self, response):
        person = models.Person.objects.all().first()
        serializer = serializers.PersonModelSerializer(person)
        print(serializer.data)
        return JsonResponse(serializer.data)
