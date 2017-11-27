# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/17 下午5:36
# @File    : users_model.py.py


from sqlalchemy import Column, String, DateTime, Integer, Numeric, BigInteger, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship
from flask_security import UserMixin
from base_model import BaseModel
from testcase_model import testcase_users
from apps.extensions import db
from apps.utils import encodeutf8


class Users(BaseModel, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=True)
    login_count = Column(Integer, default=0)
    last_login_ip = Column(String(128), default='unknown')
    email = Column(String(256), unique=True)
    password = Column(String(256))
    active = Column(Boolean())
    test_cases = relationship('TestCase', secondary=testcase_users, backref="users")

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)
        self.name = kwargs['name']
        self.email = kwargs['email']

    @staticmethod
    def get_all_mail():
        return encodeutf8(db.session.query(Users.email).all())


    @staticmethod
    def get_user_data():
        return db.session.query(Users.id, Users.name, Users.email)
