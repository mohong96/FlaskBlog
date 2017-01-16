#coding:utf-8
#文件说明：初始化app文件夹


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_TRACK_MODIFICATIONS,SQLALCHEMY_COMMIT_ON_TEARDOWN,SQLALCHEMY_MIGRATE_REPO,SQLALCHEMY_DATABASE_URI


#--创建Flask核心实例--
appweb = Flask(__name__,static_folder='static'and'imm')

#--导入配置文件--
appweb.config['SECRET_KEY'] = 'dhl19960203'

#--数据库设置--
appweb.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
appweb.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = SQLALCHEMY_COMMIT_ON_TEARDOWN
appweb.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
appweb.config['SQLALCHEMY_MIGRATE_REPO'] = SQLALCHEMY_MIGRATE_REPO

#--创建数据库对象，即SQLAlchemy的实例，与appweb结合--
db = SQLAlchemy(appweb)

# --在初始化时导入视图，否则网站视图无应答--
from app import views,models