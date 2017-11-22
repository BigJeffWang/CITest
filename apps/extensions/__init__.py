# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/17 下午5:12
# @File    : __init__.py


from flask_sqlalchemy import SQLAlchemy
from flask_mako import MakoTemplates
from contextlib import contextmanager


db = SQLAlchemy()
mako = MakoTemplates()


