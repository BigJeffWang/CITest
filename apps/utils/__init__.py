# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/19 下午11:59
# @File    : __init__.py.py


import uuid
import time
import os
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import random
import string


def get_values(values):
    tmp = {}
    for key in values:
        tmp[key] = values.get(key).encode('utf8').replace("'", "\"").replace("\n", "").replace("\t", "").replace("\r", "")
    return tmp


def get_hash_id():
    return '%s%s' % (time.strftime("%Y%m%d%H%M%S", time.localtime()), get_random_str(6))


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "/" + fn))
    file_new = ""
    if lists:
        file_new = os.path.join(testreport, lists[-1])
    return file_new


def send_mail(file_path, to_users):
    _user = "wangye@licaifan.com"
    _pwd = "Wrtx123"
    _to = to_users
    _subject = "自动化测试报告"

    with open(file_path, 'rb') as f:
        mail_body = f.read()

    msg = MIMEText(mail_body, 'html', 'utf-8')

    msg['Subject'] = Header(_subject, "utf-8")
    msg["From"] = _user
    msg["To"] = Header(",".join(_to), 'utf-8')

    # try:
    s = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    # except smtplib.SMTPException,e:


def get_random_str(num):
    str1 = "".join([str(i) for i in range(10)])
    str2 = string.ascii_letters
    return "".join(random.sample(str1 + str2, num))


def encodeutf8(data):
    tmp_list = []
    for t in data:
        tmp_tuple = []
        for i in t:
            if isinstance(i, unicode):
                tmp_tuple.append(i.encode('utf8'))
            else:
                tmp_tuple.append(i)
        tmp_list.append(tmp_tuple)
    return tmp_list


def del_old_file(file_path, reserve_count, buffer_count):
    """

    :param file_path:
    :param reserve_count: 删掉文件后所保留剩余个数
    :param buffer_count: 缓冲个数,超出缓冲个数,将会按创建时间,删掉文件时间较旧的文件
    :return:
    """
    if len(os.listdir(file_path)) > buffer_count:
        file_list = [os.sep.join([file_path, v]) for v in os.listdir(file_path)]
        file_list.sort(key=lambda fn: os.path.getmtime(fn), reverse=True)
        for i in file_list[reserve_count:]:
            os.remove(i)





# mystring=replace(mystring,chr(39),"&acute;") '替换单引号
#
# mystring=replace(mystring,chr(34),"&quot;")    '替换双引号
#
# mystring=replace(mystring,"<","&lt;")    '替换<
#
# mystring=replace(mystring,">","&gt;")    '替换>
#
# mystring=replace(mystring,chr(13),"<br>") '替换回车符
#
# mystring=replace(mystring,chr(32),"&nbsp;") '替换空格符
#
# mystring=replace(mystring,chr(9),"&nbsp; &nbsp; &nbsp; &nbsp;") '替换tab符
