from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import viewsets

from app.models import Book
from app.serializers import GroupSerializers, UserSerializers, BookSerializer


def index(request):
    return HttpResponse('Index')


class Hello(View):
    msg = 'none'

    def get(self, request):
        return HttpResponse('hello' + self.msg)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
