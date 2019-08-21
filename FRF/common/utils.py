import uuid

from flask import request

from flask_tpp.config import USER_CLIENT, CINEMA_CLIENT, USER_CLIENT_TOKEN_PREFIX, CINEMA_CLIENT_TOKEN_PREFIX
from flask_tpp.ext import cache
from user_client.model import UserModel


class IdentException(Exception):
    pass


class GetTokenException(Exception):
    pass


def get_user(ident='', client=None):
    if client not in [USER_CLIENT, CINEMA_CLIENT]:
        raise IdentException('用户表示必须为客户端用户或者影院用户 {} 或 {} 填入的为 {}' \
                             .format(USER_CLIENT, CINEMA_CLIENT, client))

    if client == USER_CLIENT:
        if ident.isdigit():
            user = UserModel.query.filter_by(phone=ident).first()
            if user:
                return user

        else:
            user = UserModel.query.filter_by(username=ident).first()
            if user:
                return user
        return None
    elif client == CINEMA_CLIENT:
        # if ident.isdigit():
        #     user = UserModel.query.filter(phone=ident).first()
        #     if user:
        #         return user
        #
        # if not ident.isdigit():
        #     user = UserModel.query.filter(username=ident).first()
        #     if user:
        #         return user
        # return None
        pass

    return None


# 获取客户端用户
def get_user_client(ident):
    return get_user(ident, client=USER_CLIENT)


# 获取影院端用户
def get_cinema_client(ident):
    return get_user(ident, client=CINEMA_CLIENT)


def generate_token(token_prefix):
    return token_prefix + uuid.uuid4().hex


# 生产客户端token
def generate_user_client_token():
    return generate_token(USER_CLIENT_TOKEN_PREFIX)


# 生成影院端token
def generate_cinema_client_token():
    return generate_token(CINEMA_CLIENT_TOKEN_PREFIX)


# 获取token
def get_token(client=None):
    if client not in [USER_CLIENT, CINEMA_CLIENT]:
        raise GetTokenException('获取token失败')
    token = request.headers.get('token', '')
    # print(token)
    if (client == USER_CLIENT and token.startswith(USER_CLIENT_TOKEN_PREFIX)) or (
            client == CINEMA_CLIENT and token.startswith(CINEMA_CLIENT_TOKEN_PREFIX)):
        return token
    return None


def get_user_client_token():
    return get_token(client=USER_CLIENT)


def get_cinema_client_token():
    return get_token(client=CINEMA_CLIENT)


# 通过token获取用户id
def use_token_get_id(token):
    if not token:
        return None
    id = None
    if token.startswith(USER_CLIENT_TOKEN_PREFIX) or token.startswith(CINEMA_CLIENT_TOKEN_PREFIX):
        id = cache.get(token)
    return id
