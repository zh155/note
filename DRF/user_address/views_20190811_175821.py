import uuid

from django.core.cache import cache
from rest_framework import viewsets, exceptions, status
from rest_framework.response import Response

from user_address import serializers, authentications, permissions, throttles
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer

    user_model = serializers.UserSerializer.Meta.model
    user = None

    def register_login(self, request, *args, **kwargs):
        action = request.query_params.get('action') or ''
        action = action.lower()
        if action not in ['register', 'login']:
            raise exceptions.APIException(detail='请确认操作')

        if action == 'register':
            return self.register(request, *args, **kwargs)
        elif action == 'login':
            return self.login(request, *args, **kwargs)

    def perform_create(self, serializer):
        # password_hash = make_password(serializer.validated_data.get('password'))
        # serializer.save(password=password_hash)
        serializer.save()

    def register(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def login(self, request, *args, **kwargs):
        name = request.data.get('name')
        password = request.data.get('password')
        try:
            user = self.user_model.objects.get(name=name)
            if user.password == password:
                self.user = user
            else:
                raise exceptions.APIException(detail='用户名/密码错误')
        except:
            raise exceptions.APIException(detail='用户名/密码错误')

        token = uuid.uuid4().hex
        cache.set(token, self.user.id, timeout=60 * 60 * 24)

        data = {
            'status': status.HTTP_200_OK,
            'msg': '登陆成功',
            'data': serializers.UserSerializer(self.user).data,
            'token': token,
        }
        return Response(data)


class AddressViewSet(viewsets.ModelViewSet):
    user_model = serializers.UserSerializer.Meta.model
    address_model = serializers.AddressSerializer.Meta.model
    serializer_class = serializers.AddressSerializer
    authentication_classes = (authentications.UserAuth,)
    permission_classes = (permissions.UserLoginPermission,)
    # 自定义限流
    # throttle_classes = (throttling.AddressThrottling,)
    # 游客限流
    # throttle_classes = (AnonRateThrottle,)
    # 用户限流    UserRateThrottle, AnonRateThrottle 同时存在时  未登录 用户访问频率也受 UserRateThrottle影响  以频率低的为准
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    # 视图范围截流
    # throttles_classes = (ScopedRateThrottle,)
    # throttle_classes = (AnonRateThrottle, UserRateThrottle, ScopedRateThrottle)
    queryset = address_model.objects.all()

    throttle_scope = 'user_address_throttle_scope'

    # user = None

    def create_address(self, request, *args, **kwargs):
        # self.required_login(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.user)
        serializer.save(user=self.request.user)

    def show_address(self, request, *args, **kwargs):
        # self.required_login(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        # 获取用户创建的
        # if isinstance(self.request.user, self.user_model):
        # 非游客用户 获取用户创建的
        if self.request.user.is_authenticated:
            return queryset.filter(user=self.request.user).all()
        # 获取所有的，不验证登录
        return queryset.all()

    def required_login(self, request, *args, **kwargs):
        token = request.META.get('HTTP_TOKEN') or ''
        user_id = cache.get(token)
        try:
            user = self.user_model.objects.get(pk=user_id)
            self.user = user
        except:
            raise exceptions.NotFound('请登录后操作')

    def del_address(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        print(self.get_object())
        print('##########')
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        # instance.delete()
        pass
    # def get_object(self):
    #     return '############'
