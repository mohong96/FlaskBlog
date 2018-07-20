#coding:utf-8
#文件说明：初始化app文件夹


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_TRACK_MODIFICATIONS,SQLALCHEMY_COMMIT_ON_TEARDOWN,SQLALCHEMY_MIGRATE_REPO,SQLALCHEMY_DATABASE_URI
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


#--创建Flask核心实例--
appweb = Flask(__name__)

#--导入配置文件--
appweb.config['SECRET_KEY'] = 'dhl19960203'

#--数据库设置--
appweb.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
appweb.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = SQLALCHEMY_COMMIT_ON_TEARDOWN
appweb.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
appweb.config['SQLALCHEMY_MIGRATE_REPO'] = SQLALCHEMY_MIGRATE_REPO

#--创建数据库对象，即SQLAlchemy的实例，与appweb结合--
db = SQLAlchemy(appweb)

#--初始话flask-login--
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.init_app(appweb)#--在flask实例中载入login_manager--

#--初始化flask-bootstrap，一个简易的bootstrap框架--
bootstrap = Bootstrap(appweb)
# --在初始化时导入视图，否则网站视图无应答--
from . import views,models