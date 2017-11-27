# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/17 下午5:36
# @File    : testcase_model.py.py


from base_model import BaseModel
from sqlalchemy import Column, String, DateTime, Integer, Numeric, BigInteger, Boolean, Table, ForeignKey, Text
from apps.extensions import db

testcase_users = Table(
    'testcase_users', BaseModel.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('test_id', Integer, ForeignKey('test_case.id'))
)


class TestCase(BaseModel):
    __tablename__ = 'test_case'
    id = Column(Integer, primary_key=True)  # 测试id
    name = Column(String(128), nullable=True)  # 测试用例名字
    url = Column(String(512), nullable=True)  # request url
    method = Column(String(10), default='get')  # request method
    headers = Column(String(512))  # request headers 额外
    parameters = Column(String(1024))  # request parameters 请求参数
    permission_confirm = Column(String(8), default='0')  # 是否开启权限认证 0 1
    token_confirm = Column(String(8), default='0')  # 记录token
    response_confirm = Column(String(8), default='0')  # 是否开启返回值验证 response存值和返回相同
    response_content = Column(Text)  # 是否开启返回值验证 response存值和返回相同
    hash_id = Column(String(64))  # 生成文件的hash ID
    status = Column(String(8), default='1')  # 假删除 1代表存在
    exec_status = Column(String(8), default='1')  # 状态,是否激活该测试用例 1代表激活

    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.name = kwargs['name']
        self.url = kwargs['url']
        self.method = kwargs['method']
        self.headers = kwargs['headers']
        self.parameters = kwargs['parameters']
        self.permission_confirm = kwargs['permission_confirm']
        self.token_confirm = kwargs['token_confirm']
        self.response_confirm = kwargs['response_confirm']
        self.response_content = kwargs['response_content']
        self.hash_id = kwargs['hash_id']
        self.status = kwargs['status']
        self.exec_status = kwargs['exec_status']

    @staticmethod
    def get_list_data(status):
        if status == "all":
            list_data = db.session.query(TestCase.id,
                                         TestCase.hash_id,
                                         TestCase.name,
                                         TestCase.exec_status,
                                         TestCase.status,
                                         ).all()
        else:
            list_data = db.session.query(TestCase.id,
                                         TestCase.hash_id,
                                         TestCase.name,
                                         TestCase.exec_status,
                                         TestCase.status,
                                         ).filter(TestCase.status == 1).all()
        return list_data

    @staticmethod
    def update_list_data(request_data):
        try:
            db.session.query(TestCase).filter(TestCase.id == int(request_data['id'])).update({TestCase.status: 0})
            db.session.commit()
        except:
            db.session.rollback()

    @staticmethod
    def delete_list_data(request_data):
        try:
            db.session.query(TestCase).filter(TestCase.id == int(request_data['id'])).update({TestCase.status: 0})
            db.session.commit()
            return db.session.query(TestCase.hash_id, TestCase.name).filter(TestCase.id == int(request_data['id'])).first()
        except:
            db.session.rollback()
            return ''

    @staticmethod
    def get_update_data(request_data):
        return db.session.query(TestCase).filter(TestCase.id == int(request_data['id'])).first().dump_to_dict()

    @staticmethod
    def get_update_data_set(request_data):
        try:
            db.session.query(TestCase).filter(TestCase.id == int(request_data['id'])).update({
                TestCase.name: request_data['name'],
                TestCase.url: request_data['url'],
                TestCase.method: request_data['method'],
                TestCase.headers: request_data['headers'],
                TestCase.parameters: request_data['parameters'],
                TestCase.permission_confirm: request_data['permission_confirm'],
                TestCase.token_confirm: request_data['token_confirm'],
                TestCase.response_confirm: request_data['response_confirm'],
                TestCase.response_content: request_data['response_content'],
                TestCase.status: request_data['status'],
                TestCase.exec_status: request_data['exec_status'],
            })
            db.session.commit()
        except:
            db.session.rollback()

    @staticmethod
    def get_name_data(hash_id):
        return db.session.query(TestCase.name).filter(TestCase.hash_id == hash_id).first()
