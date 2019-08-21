from flask import Flask

from flask_tpp.api import init_api
from flask_tpp.ext import init_ext
from flask_tpp.settings import envs


def create_app(env):
    app = Flask(__name__)

    # 初始化项目配置
    app.config.from_object(envs.get(env) or envs.get('default'))
    app.config.from_pyfile('./config.py')
    # 初始化 非路由相关  扩展库
    init_ext(app)

    # 初始化api
    init_api(app)

    return app
