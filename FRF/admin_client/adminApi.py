from flask import current_app
from flask_restful import Resource, reqparse, fields, marshal

from common.utils import get_admin_client, generate_admin_client_token
from flask_tpp.ext import cache

parser = reqparse.RequestParser()

login_parser = parser.copy()
login_parser.add_argument('username', type=str, location='form', required=True, help='请输入用户名')
login_parser.add_argument('password', type=str, location='form', required=True, help='请输入密码')

patch_parser = parser.copy()
patch_parser.add_argument('username', type=str, location='form', required=True, help='请输入用户名')
patch_parser.add_argument('password', type=str, location='form', required=True, help='请输入密码')
patch_parser.add_argument('new_password', type=str, location='form', required=True, help='请输入新密码')
patch_parser.add_argument('repeat_new_password', type=str, location='form', required=True, help='请输入确认新密码')

admin_user_field = {
    'name': fields.String(attribute='username'),
    'password': fields.String(attribute='_password')
}


class AdminResource(Resource):
    # 登录接口
    def post(self):
        login_args = login_parser.parse_args()
        username = login_args.get('username')
        password = login_args.get('password')
        admin_user = get_admin_client(username)
        if admin_user and admin_user.check_password(password) and admin_user.is_delete is False:
            admin_token = generate_admin_client_token()
            cache.set(admin_token, admin_user.id, timeout=current_app.config.get('ADMIN_CLIENT_TOKEN_TIMEOUT', 0))
            data = {
                'status': current_app.config.get('HTTP_OK'),
                'msg': '管理员登录成功',
                'data': marshal(admin_user, admin_user_field),
                'token': admin_token,
            }
            return data
        data = {
            'status': current_app.config.get('HTTP_GET_FAIL'),
            'msg': '用户名/密码错误/用户不存在',
        }
        return data

    # 信息修改接口
    def patch(self):
        patch_args = patch_parser.parse_args()
        username = patch_args.get('username')
        password = patch_args.get('password')
        new_password = patch_args.get('new_password')
        repeat_new_password = patch_args.get('repeat_new_password')
        admin_user = get_admin_client(username)
        if admin_user and admin_user.check_password(password) and new_password and new_password == repeat_new_password:
            admin_user.password = new_password
            admin_user.save()
            data = {
                'status': current_app.config.get('HTTP_OK'),
                'msg': '密码更改成功',
                'data': marshal(admin_user, admin_user_field)
            }
            return data
        data = {
            'status': 401,
            'msg': '更改失败'
        }
        return data

    def get(self):

        return 'admin_client_get'
