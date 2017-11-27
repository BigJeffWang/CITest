# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/17 下午4:56
# @File    : manage.py

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, Server

from apps.app import app
from apps.extensions import db

migrate = Migrate(app, db)
manager = Manager(app)


def make_shell_context():
    return {
        'db': db,
        'app': app,
    }


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(
    use_debugger=True, use_reloader=True,
    host='127.0.0.1', port=8080
))

if __name__ == '__main__':
    manager.run()
