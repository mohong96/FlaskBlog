#coding:utf-8
#文件说明：配置文件
import os

#--WTF表单配置--
CSRF_ENABLED = True #激活“跨站点请求伪造”保护
SECRET_KEY = 'dhl19960203' #在激活控制CSRF时需要的密码

#--数据库配置--
basedir = os.path.abspath(os.path.dirname(__file__)) #速度
SQLALCHEMY_DATABASE_URI ="sqlite:///" + basedir +"\\data.sqlite" #！指定数据库安装路径和名称,注意：是URI
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MIGRATE_REPO = "sqlite:///" + basedir +"\\db_respository"

