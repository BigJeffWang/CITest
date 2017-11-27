# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/19 下午2:23
# @File    : index.py.py


from apps.app import app
from flask_mako import render_template
from flask import send_from_directory
import os


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/download/<filename>')
def down_report(filename):
    report_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/templates/report/'
    return send_from_directory(report_path, filename, as_attachment=True)


@app.route('/report/<filename>')
def read_report(filename):
    return render_template('/report/'+filename)


@app.route('/downcase/<filename>')
def down_case(filename):
    spider_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/spiders/'
    return send_from_directory(spider_path, filename, as_attachment=True)
