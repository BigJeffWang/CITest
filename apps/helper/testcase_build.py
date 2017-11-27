# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/20 下午1:35
# @File    : testcase_build.py.py


import os


def get_parent_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_testcase_file(hash_id, name, flag=""):
    parent_path = get_parent_path()
    file_name = name.replace('.', '').replace(' ', '')
    tmp_testcase_file = parent_path + "/spiders/testcase_" + hash_id + "_" + file_name
    testcase_file = tmp_testcase_file + "_sta.py" if not flag else "_sta_bak.py"
    return testcase_file


def testcase_build(request_data, flag=""):
    parent_path = get_parent_path()
    template_file = parent_path + "/statics/testcase_template/" + "requests_template.py"
    hash_id = str(request_data['hash_id'])
    name = str(request_data['name'])
    testcase_file = get_testcase_file(hash_id, name, flag)
    with open(template_file, 'r') as f:
        rl = f.read()
        rl = rl % request_data
        with open(testcase_file, 'w+') as ff:
            ff.write(rl)


def testcase_delete(hash_id, name, flag):
    """

    :param hash_id:
    :param flag:
    1: 删除 文件名 testcase_hash_id_name_sta_bak.py
    0: 恢复 文件名 testcase_hash_id_name_sta.py
    :return:
    """

    testcase_file = get_testcase_file(hash_id, name, 0)
    testcase_file2 = get_testcase_file(hash_id, name, 1)
    if flag:
        if os.path.exists(testcase_file):
            os.rename(testcase_file, testcase_file2)
    else:
        if os.path.exists(testcase_file2):
            os.rename(testcase_file2, testcase_file)


def testcase_update_file(request_data, flag, new_flag):
    """

    :param request_data:
    :param flag: 1: 删除 0: 恢复
    :return:
    """
    hash_id = request_data['hash_id']
    if isinstance(hash_id, int):
        hash_id = str(hash_id)
    tmp_name = testcase_confirm_bak(hash_id, "name")
    if tmp_name:
        name = tmp_name.split('_')[2].decode("utf8")
        testcase_file = get_testcase_file(hash_id, name, flag)
        print testcase_file
        if os.path.exists(testcase_file):
            os.remove(testcase_file)
    if new_flag == 2:
        testcase_build(request_data)
    else:
        testcase_build(request_data, "_bak")


def testcase_confirm_bak(hash_id, func="other"):
    """

    :param hash_id:
    :param func: "name" 返回名字 "other" 返回找没找到_bak
    :return:
    """
    parent_path = get_parent_path()
    testcase_file_path = parent_path + "/spiders"
    testcase_list = os.listdir(testcase_file_path)
    for testcase_name in testcase_list:
        if hash_id in testcase_name:
            pre_name = os.path.splitext(testcase_name)[0]
            if func == "name":
                return pre_name
            if pre_name.find('_bak') > 0:
                return True
    return False
