# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/19 下午2:54
# @File    : test_case.py.py


from apps.app import app
from flask import request, flash, url_for, redirect
from flask_mako import render_template
from apps.utils import get_values
from apps.helper.testcase_helper import testcase_set_helper, testcase_helper, testcase_list_helper, \
    testcase_update_helper, testcase_delete_helper


@app.route('/testcase')
def testcase():
    # testcase_helper()
    flash('Execute successfully!')
    return redirect(url_for('index'))


@app.route('/testcase/set', methods=['GET', 'POST'])
def testcase_set():
    if request.method == 'GET':
        return render_template('testcase_add.html')

    elif request.method == 'POST':
        request_data = get_values(request.values)
        testcase_set_helper(request_data)

        return 'testcase successfully added!'


@app.route('/testcase/list', methods=['GET'])
def testcase_list():
    if request.method == 'GET':
        rows = testcase_list_helper()
        return render_template('testcase_list.html', **locals())


@app.route('/testcase/update', methods=['POST'])
def testcase_update():
    if request.method == 'POST':
        testcase_update_helper()
        flash('Modify successfully!')
        return redirect(url_for('testcase/list'))


@app.route('/testcase/delete', methods=['POST'])
def testcase_delete():
    if request.method == 'POST':
        testcase_delete_helper()
        flash('Delete successfully!')
        return redirect(url_for('testcase/list'))
