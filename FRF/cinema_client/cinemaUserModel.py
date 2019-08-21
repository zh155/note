from werkzeug.security import generate_password_hash, check_password_hash

from common.models import BaseModel
from flask_tpp.ext import db


class CinemaUserModel(BaseModel):
    __tablename__ = 'cinema_user'
    username = db.Column(db.String(256), unique=True)
    _password = db.Column(db.String(256), nullable=False)
    is_delete = db.Column(db.Boolean, default=False)
    is_verify = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, passwd):

        self._password = generate_password_hash(password=passwd)

    def check_password(self, passwd=None):
        if passwd is None:
            passwd = ''
        if check_password_hash(self._password, passwd):
            return True
        return False

    # def check_permission(self, permission):
    #     return permission & self.permission == permission
