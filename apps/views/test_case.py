# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/19 下午2:54
# @File    : test_case.py.py


from apps.app import app
from flask import request, flash, url_for, redirect, jsonify
from flask_mako import render_template
from apps.utils import get_values
from apps.helper.testcase_helper import testcase_set_helper, testcase_helper, testcase_list_helper, \
    testcase_update_helper, testcase_delete_helper, testcase_update_set_helper


@app.route('/testcase', methods=['POST'])
def testcase():
    if request.method == 'POST':
        testcase_helper()
        return jsonify({'msg': 'Execute successfully!'})


@app.route('/testcase/set', methods=['GET', 'POST'])
def testcase_set():
    if request.method == 'GET':
        return render_template('testcase_add.html')

    elif request.method == 'POST':
        request_data = get_values(request.values)
        res = testcase_set_helper(request_data)
        if res:
            flash('testcase successfully added!')
        return redirect(url_for('index'))


@app.route('/testcase/list/<status>', methods=['GET'])
def testcase_list(status):
    if request.method == 'GET':
        rows = testcase_list_helper(status)
        return render_template('testcase_list.html', **locals())


@app.route('/testcase/update', methods=['POST'])
def testcase_update():
    if request.method == 'POST':
        request_data = get_values(request.values)
        update_data = testcase_update_helper(request_data)
        return jsonify(update_data)


@app.route('/testcase/delete', methods=['POST'])
def testcase_delete():
    if request.method == 'POST':
        request_data = get_values(request.values)
        testcase_delete_helper(request_data)
        return jsonify({'msg': 'Delete successfully!'})


@app.route('/testcase/update/set', methods=['POST'])
def testcase_update_set():
    if request.method == 'POST':
        request_data = get_values(request.values)
        res = testcase_update_set_helper(request_data)
        if res:
            flash('Update successfully!')
        return redirect(url_for('testcase_list', status='part'))
