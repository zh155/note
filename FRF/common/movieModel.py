from common.models import BaseModel
from flask_tpp.ext import db


class MovieModel(BaseModel):
    __tablename__ = 'movies'
    '''
    insert into movies(id, showname, shownameen, director, leadingRole, type, country, 
    language, duration, screeningmodel, openday, backgroundpicture, flag, isdelete) 
    values(228830,"梭哈人生","The Drifting Red Balloon","郑来志","谭佑铭,施予斐,赵韩樱子,孟智超,李林轩","剧情,爱情,喜剧","中国大陆","汉语普通话",90,"4D"
    ,date("2018-01-30 00:00:00"),"i1/TB19_XCoLDH8KJjy1XcXXcpdXXa_.jpg",1,0);
    '''
    show_name = db.Column(db.String(256), name='showname', )
    show_name_en = db.Column(db.String(256), name='shownameen')
    director = db.Column(db.String(256))
    leading_role = db.Column(db.String(256), name='leadingRole')
    type = db.Column(db.String(256))
    country = db.Column(db.String(256))
    language = db.Column(db.String(256))
    duration = db.Column(db.Integer)
    screening_model = db.Column(db.String(256), name='screeningmodel')
    open_day = db.Column(db.Date, name='openday')
    background_picture = db.Column(db.String(256), name='backgroundpicture')
    flag = db.Column(db.Integer, default=1)
    is_delete = db.Column(db.Boolean, default=0, name='isdelete')
