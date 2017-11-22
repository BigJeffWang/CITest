# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com


from apps.app import app
from flask import request
from flask_mako import render_template
from apps.utils import get_values
from apps.helper.users_helper import users_add_helper


@app.route('/user/add', methods=['GET', 'POST'])
def user_add():
    if request.method == 'GET':
        return render_template('user_add.html')

    elif request.method == 'POST':
        request_data = get_values(request.values)
        users_add_helper(request_data)

        return 'User successfully added!'
