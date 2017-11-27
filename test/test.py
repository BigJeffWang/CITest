# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/18 下午11:36
# @File    : aaaa_sta.py


import sys
from pathlib import Path
# print sys.path.append(str(Path(__file__).resolve().parent))
# print str(Path(__file__).resolve().parent)

import time
import uuid

print time.strftime("%Y%m%d", time.localtime())


def _hash_id():
    return '%s.%s' % (time.strftime("%Y%m%d%H%M%S", time.localtime()), uuid.uuid4().hex)


print _hash_id()


file = 'spider_template.py'
import os

parent_path = os.path.dirname(os.path.abspath(__file__))

file = parent_path + '/' + file
file2 = parent_path + '/' + 'spider2.py'
print file

request_data = {"name": "user1", "url": "asdasd"}


print os.path.getmtime("spider.py")

a = u'asd'
print type(a)

if isinstance(a, unicode):
    b = a.encode('utf8')
    print b
    print type(b)


import string
import random
print string.ascii_letters

str1 = "".join([str(i) for i in range(10)])
str2 = string.ascii_letters
s = str1 + str2
print "".join(random.sample(s,6))

ss = 'aa'
print dir(ss)

l = [1,2,3,4,5]
l.sort(reverse=True)
print l
for i in l[2:]:
    print i


a = """
asd
zxc
"""

print a.replace("\n", "").replace("\t", "")


for k, v in {'a': 'bb'}.items():
    print k, v


if not "":
    print 11

headers = ""

if not headers:
    headers = {'Content-Type': 'application/json'}
print headers

a = '{  "success": "GET"}'
b = '{ "success"  :   "GET"  }'
print a == b

import json

a = json.loads(a)
b = json.loads(b)
print a
print type(a)
print a == b

assert(a == b)
