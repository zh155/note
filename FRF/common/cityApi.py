import json
import os

from flask import current_app
from flask_restful import Api, Resource, reqparse, fields, marshal, marshal_with

from common.cityModel import CityModel
from flask_tpp.ext import db

parse = reqparse.RequestParser()

single_city_field = {
    'id': fields.Integer(attribute='city_id'),
    'parent_id': fields.Integer,
    'region_name': fields.String,
    'city_code': fields.Integer,
    'pin_yin': fields.String,
    # 'letter': fields.String
}

multiple_cities_field = {
    # 'cities': fields.Nested(single_city_field)
    'cities': fields.List(fields.Nested(single_city_field))
}


class CitiesResource(Resource):
    # @marshal_with(multiple_cities_field)
    def get(self):
        cities = CityModel.query.all()
        city_dict = {}
        city_dict_field = {}
        for city in cities:
            if city.letter not in city_dict.keys():
                city_dict[city.letter] = []
            city_dict[city.letter].append(city)
        for k, v in city_dict.items():
            city_dict_field[k] = fields.List(fields.Nested(single_city_field))
        data = {
            'status': current_app.config.get('HTTP_OK'),
            'msg': '获取城市成功',
            'data': marshal(city_dict, city_dict_field)
        }
        return data


class LetterCitiesResource(Resource):
    def get(self, letter):
        letter = letter.upper()
        cities = CityModel.query.filter_by(letter=letter).all()
        if not cities:
            data = {
                'status': 400,
                'msg': '获取城市失败',
            }
            return data
        data = {
            'status': 200,
            'msg': '获取城市成功',
            # 'data': marshal(cities, fields.List(fields.Nested(single_city_field))),
            'data': marshal(cities, single_city_field),
        }
        return data


city_api = Api(prefix='/cities')
city_api.add_resource(CitiesResource, '')
city_api.add_resource(LetterCitiesResource, '/<string:letter>')
