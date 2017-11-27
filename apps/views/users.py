# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com


from apps.app import app
from flask import request, flash, url_for, redirect
from flask_mako import render_template
from apps.utils import get_values
from apps.helper.users_helper import users_add_helper, user_helper


@app.route('/user/add', methods=['GET', 'POST'])
def user_add():
    if request.method == 'GET':
        rows = user_helper()
        return render_template('user_add.html', **locals())

    elif request.method == 'POST':
        request_data = get_values(request.values)
        users_add_helper(request_data)
        flash('Execute successfully!')
        return redirect(url_for('index'))
