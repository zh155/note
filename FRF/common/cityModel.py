from common.models import BaseModel
from flask_tpp.ext import db


class CityModel(BaseModel):
    __tablename__ = 'city'

    city_id = db.Column(db.Integer, unique=True)
    parent_id = db.Column(db.Integer, default=0)
    region_name = db.Column(db.String(256), nullable=True)
    city_code = db.Column(db.Integer, unique=True, default=0)
    pin_yin = db.Column(db.String(256), nullable=True)
    letter = db.Column(db.String(256), nullable=False)
