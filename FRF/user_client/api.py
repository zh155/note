from flask import current_app, request
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with, marshal

from common.utils import get_user_client, generate_user_client_token, get_user_client_token, use_token_get_id
from flask_tpp.ext import cache
from user_client.model import UserModel

user_client_api = Api(prefix='/user_client')

parse = reqparse.RequestParser()
parse.add_argument('action', type=str, required=True, location='args', help='请确认操作')

parse_user_client_register = parse.copy()
parse_user_client_register.add_argument('username', type=str, required=True, location='form', help='请输入用户名')
parse_user_client_register.add_argument('phone', type=str, required=True, location='form', help='请输入手机号')
parse_user_client_register.add_argument('password', type=str, required=True, location='form', help='请输入密码')

parse_user_client_login = parse.copy()
parse_user_client_login.add_argument('name_or_phone', type=str, required=True, location='form', help='请输入手机号或用户名登录')
parse_user_client_login.add_argument('password', type=str, required=True, location='form', help='请输入密码登录')

parse_user_client_patch = reqparse.RequestParser()
parse_user_client_patch.add_argument('phone', type=str, location='form')
parse_user_client_patch.add_argument('old_password', type=str, location='form')
parse_user_client_patch.add_argument('new_password', type=str, location='form')
parse_user_client_patch.add_argument('repeat_new_password', type=str, location='form')

user_fields = {
    'username': fields.String,
    'password': fields.String,
    'phone': fields.String,
}
single_user_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(user_fields),
    'token': fields.String,
}


class User(Resource):
    def get(self):
        print(request.headers)
        return 'user_client'

    # 用户登录注册
    @marshal_with(single_user_fields)
    def post(self):
        args = parse.parse_args()
        action = args.get('action', '')
        action = action.lower()
        if action.lower() not in [current_app.config.get('USER_ACTION_LOGIN'),
                                  current_app.config.get('USER_ACTION_REGISTER')]:
            abort(404, message='请输入正确操作')
        # 用户注册
        if action == current_app.config.get('USER_ACTION_REGISTER'):
            user_client_register_args = parse_user_client_register.parse_args()
            username = user_client_register_args.get('username', None)
            password = user_client_register_args.get('password', None)
            phone = user_client_register_args.get('phone', None)
            '''
            判断username是否为字母数字下划线组合
            '''
            user = UserModel()
            user.username = username
            user.password = password
            user.phone = phone
            if not user.save():
                abort(404, message='添加用户失败')

            data = {
                'status': current_app.config.get('HTTP_CREATE_OK'),
                'msg': '用户创建成功',
                'data': user
            }
            return data
        # 用户登录
        if action == current_app.config.get('USER_ACTION_LOGIN'):
            user_client_login_args = parse_user_client_login.parse_args()
            ident = user_client_login_args.get('name_or_phone', None)
            password = user_client_login_args.get('password', None)
            user = get_user_client(ident=ident)

            if user and user.check_password(password) and user.is_delete is False:
                token = generate_user_client_token()
                cache.set(token, user.id, timeout=current_app.config.get('USER_CLIENT_TOKEN_TIMEOUT', 0))
                data = {
                    'status': current_app.config.get('HTTP_OK'),
                    'msg': '用户登录成功',
                    'data': user,
                    'token': token,
                }
                return data
            data = {
                'status': current_app.config.get('HTTP_GET_FAIL'),
                'msg': '用户名或密码错误',
            }
            return data

    # 用户更新
    def patch(self):
        print(get_user_client_token())
        print(use_token_get_id(get_user_client_token()))
        id = use_token_get_id((get_user_client_token()))
        if not id:
            data = {
                'status': current_app.config.get('HTTP_REQUEST_FAIL'),
                'msg': '没有指定用户'
            }
            return data
        user = UserModel.query.get(id)
        user_client_patch_args = parse_user_client_patch.parse_args()
        phone = user_client_patch_args.get('phone', None)
        old_password = user_client_patch_args.get('old_password', None)
        new_password = user_client_patch_args.get('new_password', None)
        repeat_new_password = user_client_patch_args.get('repeat_new_password', None)

        is_information_changed = False
        if phone:
            user.phone = phone
            is_information_changed = True
        if user.check_password(old_password) and new_password and new_password == repeat_new_password:
            user.password = new_password
            is_information_changed = True

        user.save()

        token = generate_user_client_token()
        cache.set(token, user.id, timeout=current_app.config.get('USER_CLIENT_TOKEN_TIMEOUT', 0))
        is_information_changed_msg = '用户信息更改成功' if is_information_changed else '用户信息没有更改'

        data = {
            'status': current_app.config.get('HTTP_OK'),
            'msg': is_information_changed_msg,
            'data': marshal(user, user_fields),
            'token': token
        }
        return data


user_client_api.add_resource(User, '')
