#coding:utf-8
#文件说明：ORM定义数据库模型的文件

from . import db
from werkzeug.security import generate_password_hash ,check_password_hash
from flask_login import UserMixin
from . import login_manager#--  . 代表的是当前的空间，__init__.py初始化运行的时候创建变量属于当前空间 .  --

#ORM方法，以后就用User来抽象的代替数据库表users，对数据库中表users的操作变成对User类的操作
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    #主键、邮箱账号、hash密码
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(64),unique = True,index = True)
    password_hash = db.Column(db.String(128))

#--login_manager必须的回调函数--
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Post(db.Model):
    __tablename__ = 'post'

    #主键、文章标题、文章保存地址
    id = db.Column(db.Integer,primary_key= True,index = True)
    title = db.Column(db.String(256),unique = True,index = True)
    address = db.Column(db.String(128))