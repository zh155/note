from flask import current_app, g
from flask_restful import Resource, reqparse, marshal, fields, abort

from cinema_client.cinemaModel import CinemaModel
from cinema_client.cinemaUserModel import CinemaUserModel
from common.decorators import cinema_client_login_required, permission_required
from common.utils import get_admin_client, generate_admin_client_token, generate_cinema_client_token, get_cinema_client
from flask_tpp.config import CINEMA_CLIENT_PERMISSION
from flask_tpp.ext import cache

parser = reqparse.RequestParser()

cinema_user_parser = parser.copy()
cinema_user_parser.add_argument('action', type=str, location='args', required=True, help='请输入操作')

cinema_user_register_parser = cinema_user_parser.copy()
cinema_user_register_parser.add_argument('username', type=str, location='form', required=True, help='请输入影院用户名')
cinema_user_register_parser.add_argument('password', type=str, location='form', required=True, help='请输入影院用户密码')

cinema_user_login_parser = cinema_user_parser.copy()
cinema_user_login_parser.add_argument('username', type=str, location='form', required=True, help='请输入影院用户名')
cinema_user_login_parser.add_argument('password', type=str, location='form', required=True, help='请输入影院用户密码')

cinema_user_field = {
    'username': fields.String(),
    'password': fields.String(),
    'is_verify': fields.Boolean,
}
cinema_field = {
    'name': fields.String(),
    'city': fields.String(),
    'district': fields.String(),
    'address': fields.String(),
    'phone': fields.String(),
    'score': fields.Integer,
    'hallnum': fields.Integer(attribute='hall_num'),
    'servicecharge': fields.Integer(attribute='service_charge'),
    'astrict': fields.Integer,
    'flag': fields.Integer,
    'isdelete': fields.Boolean(attribute='is_delete'),
    'cinemauserid': fields.Integer(attribute='cinema_user_id'),
}


class CinemaUserResource(Resource):
    # 获取影院信息
    @cinema_client_login_required
    @permission_required(permission=CINEMA_CLIENT_PERMISSION)
    def get(self):
        cinema_user = g.user

        cinema = CinemaModel.query.filter_by(cinema_user_id=cinema_user.id).all()

        data = {
            'status': current_app.config.get('HTTP_OK'),
            'msg': '获取电影成功',
            'data': marshal(cinema, cinema_field)
        }
        return data

    # 影院用户注册
    def post(self):
        cinema_user_parser_args = cinema_user_parser.parse_args()
        action = cinema_user_parser_args.get('action')

        if action == current_app.config.get('CINEMA_CLIENT_ACTION_REGISTER'):
            cinema_user_register_parser_args = cinema_user_register_parser.parse_args()
            username = cinema_user_register_parser_args.get('username')
            password = cinema_user_register_parser_args.get('password')
            cinema_user = CinemaUserModel()
            cinema_user.username = username
            cinema_user.password = password
            if not cinema_user.save():
                abort(400, message='添加影院用户失败/此用户已经存在')
            data = {
                'status': current_app.config.get('HTTP_CREATE_OK'),
                'msg': '成功添加一条影院用户',
                'data': marshal(cinema_user, cinema_user_field)
            }
            return data

        elif action == current_app.config.get('CINEMA_CLIENT_ACTION_LOGIN'):
            cinema_user_login_parser_args = cinema_user_login_parser.parse_args()
            username = cinema_user_login_parser_args.get('username')
            password = cinema_user_login_parser_args.get('password')
            cinema_user = get_cinema_client(username)
            if cinema_user and (not cinema_user.is_delete) and cinema_user.check_password(password):
                token = generate_cinema_client_token()
                cache.set(token, cinema_user.id, timeout=current_app.config.get('USER_CLIENT_TOKEN_TIMEOUT', 0))
                data = {
                    'status': current_app.config.get('HTTP_OK'),
                    'msg': '用户登录成功',
                    'data': marshal(cinema_user, cinema_user_field),
                    'token': token,
                }
                return data
            data = {
                'status': current_app.config.get('HTTP_REQUEST_FAIL'),
                'msg': '登录失败，请检查用户名/密码是否正确'
            }
            return data
        abort(400, message='请键入操作')
