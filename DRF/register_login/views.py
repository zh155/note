import uuid

from django.core.cache import cache
from rest_framework import viewsets, exceptions, status

# Create your views here.
from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response

from register_login import serializers, models


class RegisterLoginViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = serializers.UserSerializer.Meta.model.objects.all()

    def post(self, request, *args, **kwargs):
        return self.register_login(request, *args, **kwargs)

    def register_login(self, request, *args, **kwargs):
        print('dfssafsfsd')
        if request.query_params.get('action').lower() == 'login':
            pass
        elif request.query_params.get('action').lower() == 'register':
            return self.create(request, *args, **kwargs)
        else:
            raise exceptions.APIException(detail='请提供正确的参数')


class RegisterLoginAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = serializers.UserSerializer.Meta.model.objects.all()

    def post(self, request, *args, **kwargs):
        action = request.query_params.get('action') or ''
        if action.lower() == 'register':
            return self.create(request, *args, **kwargs)
        elif action.lower() == 'login':
            return self.login(request, *args, **kwargs)
        else:
            raise exceptions.APIException(detail='请提供正确的参数')

    def login(self, request, *args, **kwargs):
        name = request.data.get('name')
        password = request.data.get('password')

        try:
            user = models.User.objects.get(name=name)

        except Exception:
            raise exceptions.NotFound(detail='没有此用户')
        if not user.verify_password(password):
            raise exceptions.NotAuthenticated(detail='密码错误')
        token = uuid.uuid4().hex
        cache.set(token, user.id, timeout=60)
        data = {
            'msg': '登陆成功',
            'status': status.HTTP_200_OK,
            'token': token,
        }
        return Response(data)
