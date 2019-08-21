import datetime
import os

from flask import current_app
from flask_restful import Resource, Api, marshal, fields, reqparse, abort
from werkzeug.datastructures import FileStorage

from common.decorators import admin_client_login_required, permission_required
from common.movieModel import MovieModel
from common.utils import uploads_images_path, del_file
from flask_tpp.config import ADMIN_CLIENT_PERMISSION
from flask_tpp.ext import db

movie_field = {
    'showname': fields.String(attribute='show_name'),
    'shownameen': fields.String(attribute='show_name_en'),
    'director': fields.String(attribute='director'),
    'leadingRole': fields.String(attribute='leading_role'),
    'type': fields.String(attribute='type'),
    'country': fields.String(attribute='country'),
    'language': fields.String(attribute='language'),
    'duration': fields.Integer(attribute='duration'),
    'screeningmodel': fields.String(attribute='screening_model'),
    'openday': fields.String(attribute='open_day'),
    'backgroundpicture': fields.String(attribute='background_picture'),
    'flag': fields.Integer(attribute='flag'),
    'isdelete': fields.Boolean(attribute='is_delete'),
}

parser = reqparse.RequestParser()
movie_add_parser = parser.copy()
movie_add_parser.add_argument('show_name', location='form', type=str, required=True, help='请输入电影名称')
movie_add_parser.add_argument('show_name_en', location='form', type=str, help='请输入电影英文名称')
movie_add_parser.add_argument('director', location='form', type=str, required=True, help='请输入电影导演名称')
movie_add_parser.add_argument('leading_role', location='form', type=str, required=True, help='请输入电影主演名称')
movie_add_parser.add_argument('type', location='form', type=str, required=True, help='请输入电影类型')
movie_add_parser.add_argument('country', location='form', type=str, required=True, help='请输入电影国家或地区')
movie_add_parser.add_argument('language', location='form', type=str, required=True, help='请输入电影语言')
movie_add_parser.add_argument('duration', location='form', type=str, required=True, help='请输入电影时长')
movie_add_parser.add_argument('screening_model', location='form', type=str, required=True, help='请输入电影视觉类型')
movie_add_parser.add_argument('open_day', location='form', type=str, required=True, help='请输入电影上映时间')
movie_add_parser.add_argument('background_picture', location='files', type=FileStorage, required=True, help='请添加电影封面图片')
movie_add_parser.add_argument('flag', location='form', type=int, required=True, help='请输入电影标志')

movie_patch_parser = parser.copy()
movie_patch_parser.add_argument('show_name', location='form', type=str)
movie_patch_parser.add_argument('show_name_en', location='form')
movie_patch_parser.add_argument('director', location='form', type=str)
movie_patch_parser.add_argument('leading_role', location='form', type=str)
movie_patch_parser.add_argument('type', location='form', type=str)
movie_patch_parser.add_argument('country', location='form', type=str)
movie_patch_parser.add_argument('language', location='form', type=str)
movie_patch_parser.add_argument('duration', location='form', type=str)
movie_patch_parser.add_argument('screening_model', location='form', type=str)
movie_patch_parser.add_argument('open_day', location='form', type=str)
movie_patch_parser.add_argument('background_picture', location='files', type=FileStorage)
movie_patch_parser.add_argument('flag', location='form', type=int)
movie_patch_parser.add_argument('is_delete', location='form', type=int, help='is_delete只能为0或1')


class MoviesResource(Resource):
    def get(self):
        movies = MovieModel.query.all()
        data = {
            'status': current_app.config.get('HTTP_OK'),
            'msg': '获取电影成功',
            'data': marshal(movies, movie_field)
        }
        return data

    # 添加电影
    @admin_client_login_required
    @permission_required(permission=ADMIN_CLIENT_PERMISSION)
    def post(self):
        movie_add_parser_args = movie_add_parser.parse_args()
        show_name = movie_add_parser_args.get('show_name')
        show_name_en = movie_add_parser_args.get('show_name_en')
        director = movie_add_parser_args.get('director')
        leading_role = movie_add_parser_args.get('leading_role')
        movie_type = movie_add_parser_args.get('type')
        country = movie_add_parser_args.get('country')
        language = movie_add_parser_args.get('language')
        duration = movie_add_parser_args.get('duration')
        screening_model = movie_add_parser_args.get('screening_model')
        open_day = datetime.date(*(map(int, movie_add_parser_args.get('open_day').split('-'))))
        background_picture = movie_add_parser_args.get('background_picture')
        flag = movie_add_parser_args.get('flag')

        movie = MovieModel()
        movie.show_name = show_name
        movie.show_name_en = show_name_en
        movie.director = director
        movie.leading_role = leading_role
        movie.type = movie_type
        movie.country = country
        movie.language = language
        movie.duration = duration
        movie.screening_model = screening_model
        movie.open_day = open_day

        movie.flag = flag
        new_filename, path = uploads_images_path(filename=background_picture.filename)
        movie.background_picture = os.path.join(current_app.config.get('UPLOADS_IMAGES_REL_PATH'), new_filename)

        if not movie.save():
            try:
                movie.delete()
            except Exception:
                pass
            abort(400, message='添加电影失败')

        background_picture.save(os.path.join(current_app.config.get('UPLOADS_IMAGES_PATH'), new_filename))
        data = {
            'status': current_app.config.get('HTTP_CREATE_OK'),
            'msg': '成功添加一条电影信息',
            'data': marshal(movie, movie_field),
        }
        return data


class MovieResource(Resource):
    def get(self, id):
        movie = MovieModel.query.get(id)
        if (not movie) or movie.is_delete:
            abort(404, message='没有此电影信息')
        data = {
            'status': current_app.config.get('HTTP_OK'),
            'msg': '获取电影信息成功',
            'data': marshal(movie, movie_field)
        }
        return data

    # 修改电影信息
    @admin_client_login_required
    @permission_required(permission=ADMIN_CLIENT_PERMISSION)
    def patch(self, id):
        movie = MovieModel.query.get(id)
        if not movie:
            abort(404, message='没有此电影信息')

        movie_patch_parser_args = movie_patch_parser.parse_args()
        show_name = movie_patch_parser_args.get('show_name') or movie.show_name
        show_name_en = movie_patch_parser_args.get('show_name_en') or movie.show_name_en
        director = movie_patch_parser_args.get('director') or movie.director
        leading_role = movie_patch_parser_args.get('leading_role') or movie.leading_role
        movie_type = movie_patch_parser_args.get('type') or movie.type
        country = movie_patch_parser_args.get('country') or movie.country
        language = movie_patch_parser_args.get('language') or movie.language
        duration = movie_patch_parser_args.get('duration') or movie.duration
        screening_model = movie_patch_parser_args.get('screening_model') or movie.screening_model
        flag = movie_patch_parser_args.get('flag') or movie.flag
        is_delete = movie_patch_parser_args.get('is_delete') if movie_patch_parser_args.get(
            'is_delete') is None else movie.is_delete

        if bool(movie_patch_parser_args.get('is_delete')) != movie.is_delete:
            is_delete = not movie.is_delete

        open_day = movie_patch_parser_args.get('open_day') if movie_patch_parser_args.get(
            'open_day') else movie.open_day

        background_picture = movie_patch_parser_args.get('background_picture') or movie.background_picture

        if movie_patch_parser_args.get('background_picture'):
            old_background_picture = os.path.join(current_app.config.get('PROJECT_PATH'),
                                                  movie.background_picture)
            if not del_file(old_background_picture):
                abort(400, message='更换电影背景图失败')

            new_filename, path = uploads_images_path(filename=background_picture.filename)
            movie.background_picture = os.path.join(current_app.config.get('UPLOADS_IMAGES_REL_PATH'), new_filename)
            background_picture.save(os.path.join(current_app.config.get('UPLOADS_IMAGES_PATH'), new_filename))

        movie.show_name = show_name
        movie.show_name_en = show_name_en
        movie.director = director
        movie.leading_role = leading_role
        movie.type = movie_type
        movie.country = country
        movie.language = language
        movie.duration = duration
        movie.screening_model = screening_model
        movie.open_day = open_day
        movie.flag = flag
        movie.is_delete = is_delete
        if not movie.save():
            abort(400, message='修改电影信息失败')

        data = {
            'status': current_app.config.get('HTTP_CREATE_OK'),
            'msg': '成功更新一条电影信息',
            'data': marshal(movie, movie_field),
        }
        return data


movie_api = Api(prefix='/movies')
movie_api.add_resource(MoviesResource, '')
movie_api.add_resource(MovieResource, '/<int:id>')
