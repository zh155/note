import uuid

from django.core.cache import cache
from django.shortcuts import render

# Create your views here.

from rest_framework import views, exceptions, request, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets

from data_cascade import serializers, models


class UserAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializers
    queryset = serializers.UserSerializers.Meta.model

    # 创建用户
    def post(self, request, *args, **kwargs):
        action = request.query_params.get('action')
        if action == 'register':
            user_serializer = serializers.UserSerializers(request.data)

            # return self.create(request, *args, request.data)

            '''
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            raise exceptions.APIException(user_serializer.errors)
            '''
            return self.create(request, *args, **kwargs)
        elif action == 'login':
            try:
                user = models.User.objects.get(name=request.data.get('name'))
                if not (user and user.password == request.data.get('password')):
                    raise exceptions.APIException(detail='用户名/密码错误')
            except:
                raise exceptions.APIException(detail='用户名/密码错误')
            token = uuid.uuid4().hex
            cache.set(token, user.id, timeout=60 * 24 * 24)
            data = {
                'user': serializers.UserSerializers(user).data,
                'token': token,
            }
            return Response(data)
        raise exceptions.APIException(detail='请输入具体操作')


class BookAPIView(generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView,
                  generics.DestroyAPIView):
    serializer_class = serializers.BookSerializers
    queryset = serializers.BookSerializers.Meta.model.objects.all()

    def post(self, request, *args, **kwargs):
        '''
        创建书
        :param request:
        :param args:
        :param kwargs:
        :return: 创建成功的书
        '''
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        '''
        获取所有书
        :param request:
        :param args:
        :param kwargs:
        :return: 所有书
        '''
        print(request)
        return self.list(request, *args, **kwargs)


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializers
    queryset = serializers.BookSerializers.Meta.model.objects.all()
    user = None
    token = None

    def required_login(self, request, *args, **kwargs):
        '''
        验证登录
        :return:
        '''
        token = request.META.get('HTTP_TOKEN')
        self.token = token
        try:
            user_id = cache.get(token)
            user = models.User.objects.get(pk=user_id)
            self.user = user
        except:
            raise exceptions.APIException(detail='请重新登录')

    def do_post(self, request, *args, **kwargs):
        '''
        创建书籍
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        self.required_login(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.user)

    def do_destroy(self, request, *args, **kwargs):
        self.required_login(request, *args, **kwargs)
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not (instance.user == self.user):
            raise exceptions.APIException(detail='只能删除属于自己的书籍')
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def retrieve(self, request, *args, **kwargs):
        '''
        获取任一本书
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        return super().retrieve(request, *args, **kwargs)

    def do_retrieve(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
