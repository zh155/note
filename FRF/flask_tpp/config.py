import os

PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
NONE_PERMISSION = 0
USER_CLIENT_PERMISSION = 1
CINEMA_CLIENT_PERMISSION = 2
ADMIN_PERMISSION = 4

HTTP_CREATE_OK = 201
HTTP_OK = 200
HTTP_REQUEST_FAIL = 400

USER_ACTION_LOGIN = 'login'
USER_ACTION_REGISTER = 'register'

USER_CLIENT_IDENT = 'user_client'
CINEMA_CLIENT_IDENT = 'cinema_client'

USER_CLIENT = 'user_client'
CINEMA_CLIENT = 'cinema_client'

USER_CLIENT_TOKEN_PREFIX = 'user_client_'
CINEMA_CLIENT_TOKEN_PREFIX = 'cinema_client_'

USER_CLIENT_TOKEN_TIMEOUT = 60 * 24 * 24
CINEMA_CLIENT_TOKEN_TIMEOUT = 60 * 24 * 24