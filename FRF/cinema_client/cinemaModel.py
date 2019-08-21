from cinema_client.cinemaUserModel import CinemaUserModel
from common.models import BaseModel
from flask_tpp.ext import db


class CinemaModel(BaseModel):
    '''
    insert into cinemas(name,city,district,address,phone,score,hallnum,servicecharge,astrict,flag,isdelete)
    values("深圳戏院影城","深圳","罗湖","罗湖区新园路1号东门步行街西口","0755-82175808",9.7,9,1.2,20,1,0);
    '''
    __tablename__ = 'cinemas'
    name = db.Column(db.String(256), name='name')
    city = db.Column(db.String(256), name='city')
    district = db.Column(db.String(256), name='district')
    address = db.Column(db.String(256), name='address')
    phone = db.Column(db.String(256), name='phone')
    score = db.Column(db.Integer, name='score')
    hall_num = db.Column(db.Integer, name='hallnum')
    service_charge = db.Column(db.Integer, name='servicecharge')
    astrict = db.Column(db.Integer, name='astrict')
    flag = db.Column(db.Integer, name='flag')
    is_delete = db.Column(db.Boolean, name='isdelete')
    cinema_user_id = db.Column(db.Integer, db.ForeignKey(CinemaUserModel.id), default=1)
