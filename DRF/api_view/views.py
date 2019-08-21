from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from api_view import serializers
from api_view.models import Student


def Index(request):
    print(request)
    print(type(request))
    return HttpResponse('Index')


@api_view(['get', 'post'])
def Api(request):
    print(request)
    print(type(request))
    # return HttpResponse('Index')
    return Response('Index')


class ApiView(APIView):
    def get(self, request):
        print(request)
        print(type(request))

        return Response('APIView')


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = Student.objects.all()


class StudentCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.StudentSerializer


class StudentListAPIView(generics.ListAPIView):
    serializer_class = serializers.StudentSerializer
    queryset = serializers.StudentSerializer.Meta.model.objects.all()


class StudentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.StudentSerializer
    queryset = serializers.StudentSerializer.Meta.model.objects.all()


class StudentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.StudentSerializer
    queryset = serializers.StudentSerializer.Meta.model.objects.all()


class StudentModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = serializers.StudentSerializer.Meta.model.objects.all()
