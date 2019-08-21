from admin import admin_api
from cinema_client import cinema_client_api
from user_client import user_client_api


def init_api(app):
    user_client_api.init_app(app)
    admin_api.init_app(app)
    cinema_client_api.init_app(app)
