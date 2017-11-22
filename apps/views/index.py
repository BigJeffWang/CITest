# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/19 下午2:23
# @File    : index.py.py


from apps.app import app
from flask_mako import render_template
from flask import send_from_directory
import os


report_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/report/'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/<filename>')
def report(filename):
    return send_from_directory(report_path, filename, as_attachment=True)
