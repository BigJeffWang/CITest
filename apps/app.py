# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/17 下午5:19
# @File    : app.py

import os
from flask import Flask
from config import config
from apps.extensions import mako, db

config_name = "development"
instance_path = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, instance_path=instance_path, template_folder='templates', static_folder='statics')
app.config.from_object(config[config_name])

mako.init_app(app)
db.init_app(app)

