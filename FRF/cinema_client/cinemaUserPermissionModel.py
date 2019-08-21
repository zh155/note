from common.models import BaseModel
from flask_tpp.ext import db


class Permissions(BaseModel):
    __tablename__ = 'permissions'

    p_name = db.Column(db.String(256), unique=True)


class CinemaUserPermission(BaseModel):
    __tablename__ = 'cinema_user_permission'

    cinema_user_id = db.Column(db.Integer, db.ForeignKey('cinema_user.id'))
    cinema_permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'))
