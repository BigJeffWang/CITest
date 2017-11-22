# coding=utf-8
# @Author  : WangYe
# @contact:  bigjeffwang@163.com
# @Time    : 2017/11/18 下午11:02
# @File    : base_model.py


import datetime
import uuid

from decimal import Decimal
from sqlalchemy import Column, BigInteger, Boolean
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    update_at = Column(DateTime, onupdate=datetime.datetime.now)
    deleted = Column(Boolean, default=False)  # 是否删除
    deleted_at = Column(DateTime)

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)
        self.created_at = datetime.datetime.now()

    def dump_to_dict(self):
        ret = {}
        for name in self.__table__.columns.keys():
            if isinstance(getattr(self, name), datetime.datetime):
                ret[name] = str(getattr(self, name))
            elif isinstance(getattr(self, name), Decimal):
                ret[name] = float(getattr(self, name))
            else:
                ret[name] = getattr(self, name)
        return ret

    def set_by_dict(self, args):
        keys = self.__table__.columns.keys()
        for k in args:
            if k not in keys:
                raise Exception("set a unknown key:%s" % k)
            setattr(self, k, args[k])

    def delete(self, session):
        self.deleted = True
        self.deleted_at = datetime.datetime.now()
        session.commit()

    def uuid(self):
        return uuid.uuid4().hex
