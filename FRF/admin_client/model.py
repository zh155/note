from werkzeug.security import generate_password_hash, check_password_hash

from common.models import BaseModel
from flask_tpp.config import ADMIN_CLIENT_PERMISSION
from flask_tpp.ext import db


class AdminModel(BaseModel):
    __tablename__ = 'admin_client'
    username = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))
    is_delete = db.Column(db.Boolean, default=False)
    permission = db.Column(db.Integer, default=ADMIN_CLIENT_PERMISSION)

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

    def check_permission(self, permission):
        return (not self.is_delete) and (permission & self.permission == permission)
