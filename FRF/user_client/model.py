from werkzeug.security import generate_password_hash, check_password_hash

from flask_tpp.config import NONE_PERMISSION
from flask_tpp.ext import db
from common.models import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'user'
    username = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))
    phone = db.Column(db.String(32), unique=True)
    is_delete = db.Column(db.Boolean, default=False)
    permission = db.Column(db.Integer, default=NONE_PERMISSION)

    @property
    def password(self):
        return None

    @password.setter
    def password(self, passwd):

        self._password = generate_password_hash(password=passwd)

    def check_password(self, passwd=None):
        if passwd is None:
            passwd = ''
        if check_password_hash(self._password, passwd):
            return True
        return False
