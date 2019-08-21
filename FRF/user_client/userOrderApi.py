from flask import current_app, g
from flask_restful import Resource, reqparse

from common.decorators import user_client_login_required, permission_required

parse = reqparse.RequestParser()


class UserOrdersResource(Resource):
    def get(self):
        return 'userinfo orders resource'


class UserOrderResource(Resource):

    def get(self, order_id):
        return 'userinfo order resource'

    @user_client_login_required
    @permission_required(permission='VIP_USER_CLIENT_PERMISSION')
    def put(self, order_id):
        return 'fdsafsda'
