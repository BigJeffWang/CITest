# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/19 下午2:54
# @File    : test_case.py.py


from apps.app import app
from flask import request
from flask_mako import render_template
from apps.utils import get_values
from apps.helper.testcase_helper import testcase_set_helper, testcase_helper


@app.route('/testcase/set', methods=['GET', 'POST'])
def testcase_set():
    if request.method == 'GET':
        return render_template('testcase_add.html')

    elif request.method == 'POST':
        request_data = get_values(request.values)
        testcase_set_helper(request_data)

        return 'testcase successfully added!'


@app.route('/testcase')
def testcase():
    testcase_helper()
    return 'The test was successful and the message was sent!'


@app.route('/testcase/list', methods=['GET', 'POST'])
def testcase_list():
    if request.method == 'GET':
        rows = [['id', 'name', 'status'], [123123, '斯蒂芬斯蒂芬', 1], [123123, '斯蒂芬斯蒂芬', 0]]
        return render_template('testcase_list.html', **locals())

    elif request.method == 'POST':
        request_data = get_values(request.values)
        testcase_set_helper(request_data)

        return 'testcase successfully updated!'
