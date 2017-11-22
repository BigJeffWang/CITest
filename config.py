# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/17 下午5:24
# @File    : config.py


import os

PROJECT_NAME = 'AutomationTest'


def get_basedir():
    basedir = os.path.abspath(os.path.dirname(__file__))
    basedir = basedir[:basedir.find(PROJECT_NAME) + len(PROJECT_NAME)]
    return basedir

# def makedir(dirs):
#     tmpdir = os.path.join(get_basedir(), dirs)
#     if not os.path.exists(tmpdir):
#         os.makedirs(tmpdir)
#     return tmpdir


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret string'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    TMP_UPLOAD_FOLDER = 'apps/templates/tmp/uploads'
    BASEDIR = get_basedir()
    UPLOAD_FOLDER = 'apps/templates/tmp/permdir'

    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = 'super-'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://root:root@localhost:3306/test'
    SQLALCHEMY_BINDS = {
        'data': 'mysql://root:root@localhost:23306/test'
    }

    REDIS_URL = 'redis://127.0.0.1:6379/0'
    LOGGER_FILE = os.path.join(Config.BASEDIR, 'logs/mysql_sqlalchemy.log')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(Config.BASEDIR, 'test')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(Config.BASEDIR, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
