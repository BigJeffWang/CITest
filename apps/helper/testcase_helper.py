# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/20 上午9:54
# @File    : testcase_helper.py


from apps.models.testcase_model import TestCase
from apps.models.users_model import Users
from apps.extensions import db
from testcase_build import testcase_build
from apps.utils import get_hash_id, new_report, send_mail, del_old_file
import time
from HTMLTestRunner import HTMLTestRunner
import unittest
import os


def testcase_set_helper(request_data):
    request_data['hash_id'] = get_hash_id()
    request_data['status'] = 1  # 默认配置增加直接激活
    testcase = TestCase(name=request_data['name'],
                        url=request_data['url'],
                        method=request_data['method'],
                        headers=request_data['headers'],
                        parameters=request_data['parameters'],
                        permission_confirm=request_data['permission_confirm'],
                        token_confirm=request_data['token_confirm'],
                        response_confirm=request_data['response_confirm'],
                        response_content=request_data['response_content'],
                        hash_id=request_data['hash_id'],
                        status=request_data['status'])

    try:
        db.session.add(testcase)
        db.session.commit()
    except:
        db.session.rollback()

    testcase_build(request_data)


def testcase_helper():
    report_file = "/" + time.strftime("%Y_%m_%d_%H_%M_%S") + '_report.html'
    parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    report_path = parent_path + '/report'
    testcase_path = parent_path + '/spiders'
    filename = report_path + report_file
    description = "具体执行报告请点击链接下载查看: http://127.0.0.1:5000" + report_file
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='RollingStone自动化测试报告',
            description=description
        )

        discover = unittest.defaultTestLoader.discover(
            testcase_path,
            pattern='*_sta.py'
        )
        runner.run(discover)
    del_old_file(report_path, 10, 30)
    file_path = new_report(report_path)
    to_users = []
    [to_users.extend(i) for i in Users.get_all_mail()]
    send_mail(file_path, to_users)
