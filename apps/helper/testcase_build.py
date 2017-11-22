# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/20 下午1:35
# @File    : testcase_build.py.py


import os


def testcase_build(request_data):
    parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_file = parent_path + "/statics/testcase_template/" + "spider_template.py"
    testcase_file = parent_path + "/spiders/testcase" + str(request_data['hash_id']) + "_sta.py"
    with open(template_file, 'r') as f:
        rl = f.read()
        rl = rl % request_data
        with open(testcase_file, 'w+') as ff:
            ff.write(rl)


