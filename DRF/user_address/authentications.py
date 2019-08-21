from django.core.cache import cache
from rest_framework import authentication

from user_address import models


class UserAuth(authentication.BaseAuthentication):

    def authenticate(self, request):
        try:
            token = request.MEAT.get('HTTP_TOKEN')
            user_id = cache.get('token')
            user = models.User.objects.get(user_id)
            return user, token
        except:
            return
