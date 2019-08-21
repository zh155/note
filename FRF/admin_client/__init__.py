from flask_restful import Api

from admin_client.adminApi import AdminResource

admin_api = Api(prefix='/admin_client')
admin_api.add_resource(AdminResource, '')
