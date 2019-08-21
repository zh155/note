from rest_framework.permissions import BasePermission

from user_address import models


class UserLoginPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method.lower() == 'get':
            return True
        return isinstance(request.user, models.User)
