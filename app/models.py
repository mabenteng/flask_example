from enum import unique
from alembic.script import base
from werkzeug.security import check_password_hash, generate_password_hash
from app.ext import db


class basemodel(db.Model):
    __abstract__=True
    id=db.Column(db.Integer,primary_key=True)
    # 定义通用的保存方法
    def save(self):
        db.session.add(self)
        db.session.commit()



# 下面开始定义表,继承上面基类basemodel
class User(basemodel):
    name=db.Column(db.String(30),nullable=True)
    addr= db.Column(db.String(50))
    age=db.Column(db.String(60),nullable=True)



# 搞一个vip表用来注册登录网站
class Vip(basemodel):
    username=db.Column(db.String(40))
    pwd=db.Column(db.String(400))
    phone=db.Column(db.String(15))


# 搞一个Second表用来引入bootstrap注册登录网站,且模型引入密码检查设置
class Second(basemodel):
    username=db.Column(db.String(40))
    pwd=db.Column(db.String(400))
    phone=db.Column(db.String(15))
    @property
    def pwdhash(self):
        print("不能访问密码字段")
        raise AttributeError("不能直接查看密码字段")
    
    @pwdhash.setter
    def pwdhash(self,value):
        '''定义改变保存密码pwd为hash值'''
        self.pwd=generate_password_hash(value)

    def checkpwd(self,pwd):
        '''登录将用户输入的密码与数据库做对比'''
        if check_password_hash(self.pwd,pwd):
            return True
        return False

