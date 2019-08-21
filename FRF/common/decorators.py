import functools

from flask import current_app, g
from flask_restful import abort

from admin_client.model import AdminModel
from cinema_client.cinemaUserModel import CinemaUserModel
from common.utils import use_token_get_id, get_user_client_token, get_admin_client_token, get_cinema_client_token
from flask_tpp.config import COMMON_USER_CLIENT_PERMISSION, VIP_USER_CLIENT_PERMISSION, ADMIN_CLIENT_PERMISSION, \
    CINEMA_CLIENT_PERMISSION


# 验证登录
def login_required(client=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if client.lower() == 'user_client':
                from user_client.userModel import UserModel
                id = use_token_get_id(get_user_client_token()) or None
                try:
                    user = UserModel.query.get(id)
                    if not user:
                        abort(400, message='请登录后操作')
                    g.user = user
                except Exception:
                    abort(400, message='请登录后操作')
                return func(*args, **kwargs)
            elif client.lower() == 'cinema_client':
                cinema_user_id = use_token_get_id(get_cinema_client_token()) or None
                try:
                    cinema_user = CinemaUserModel.query.get(cinema_user_id)
                    if not cinema_user:
                        abort(400, message='请登录后操作')
                    g.user = cinema_user
                except Exception:
                    abort(400, message='请登录后操作')

                return func(*args, **kwargs)

            elif client.lower() == 'admin_client':
                admin_id = use_token_get_id(get_admin_client_token()) or None
                try:
                    user = AdminModel.query.get(admin_id)
                    if not user:
                        abort(400, message='请登录后操作')
                    g.user = user
                except Exception:
                    abort(400, message='请登录后操作')
                return func(*args, **kwargs)
            abort(400, message='请登录后操作')

        return wrapper

    return decorator


# 验证用户端登录
user_client_login_required = login_required(client='user_client')

# 验证影院端登录
cinema_client_login_required = login_required(client='cinema_client')

# 验证管理员登录
admin_client_login_required = login_required(client='admin_client')


# 验证权限
def permission_required(permission=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user = g.user

            # 是否为黑名单用户
            def black_user():
                if user.check_permission(current_app.config.get('BLACK_USER_CLIENT_PERMISSION')):
                    return True
                return False

            # 是否为普通用户
            def common_user():
                if user.check_permission(current_app.config.get('COMMON_USER_CLIENT_PERMISSION')):
                    return True
                return False

            # 是否为VIP用户
            def vip_user():
                if user.check_permission(current_app.config.get('VIP_USER_CLIENT_PERMISSION')):
                    return True
                return False

            # 是否为管理员用户
            def admin_user():
                if user.check_permission(current_app.config.get('ADMIN_CLIENT_PERMISSION')):
                    return True
                return False

            # 是否为影院端用户
            # def cinema_user():
            #     if user.check_permission(current_app.config.get('CINEMA_CLIENT_PERMISSION')):
            #         return True
            #     return False

            # 验证普通用户权限
            if permission == COMMON_USER_CLIENT_PERMISSION:
                if not ((not black_user()) and common_user()):
                    abort(401, message='没有普通用户权限')

            # 验证VIP用户权限
            elif permission == VIP_USER_CLIENT_PERMISSION:
                if not ((not black_user()) and common_user() and vip_user()):
                    abort(401, message='没有VIP用户权限')

            elif permission == ADMIN_CLIENT_PERMISSION:
                if not admin_user():
                    abort(401, message='没有管理员权限')

            elif permission == CINEMA_CLIENT_PERMISSION:
                if not ((not user.is_delete) and user.is_verify):
                    abort(401, message='没有影院用户权限或没有认证')

            else:
                abort(401, message='没有权限')
            return func(*args, **kwargs)

        return wrapper

    return decorator
