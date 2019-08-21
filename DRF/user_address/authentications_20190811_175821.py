from django.core.cache import cache
from rest_framework import authentication

from user_address import models


class UserAuth(authentication.BaseAuthentication):

    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_TOKEN')
            user_id = cache.get(token)

            user = models.User.objects.get(pk=user_id)

            # 登录的用户不截流
            user.is_authenticated = True

            # 认证成功  user token 会存在request上
            return user, token
        except Exception as e:
            if request.method.lower() == 'get':
                return models.User(), True
            return False
