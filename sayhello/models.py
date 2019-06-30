# 定义数据库模型

from datetime import datetime
from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    # timestamp 用来储存每一条留言的时间，这个字段存储的是python的datetime对象，、
    # index = True，开启索引，用default参数设置了默认值
    '''
    这里用的是datetime.utcnow, 而不是datetime.utcnow()，这里要传入的是需要调用
    的方法，而不是调用方法后返回的对象.
    sqlalchemy 会在创建新的数据库记录的时候，也就是用户提交message的时候，调用该对象
    设置默认值，如果传入的是uctnow()，这里方法就会在载入模块的时候执行.
    
    '''

