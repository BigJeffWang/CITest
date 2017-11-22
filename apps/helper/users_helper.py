# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com


from apps.models.users_model import Users
from apps.extensions import db


def users_add_helper(request_data):
    user = Users(name=request_data['name'],
                 email=request_data['email'],
                 )

    try:
        db.session.add(user)
        db.session.commit()
    except:
        db.session.rollback()
