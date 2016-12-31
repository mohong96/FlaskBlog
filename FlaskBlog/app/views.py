#coding:utf-8
#文件说明：定义网站视图函数的文件



from app import appweb,db
from flask import render_template,url_for,session,redirect

@appweb.route('/home')
@appweb.route('/')
def home():
    return render_template('home.html')


@appweb.route('/project')
def project():
    return render_template('project.html')


@appweb.route('/article')
def article():
    return render_template('article.html')


@appweb.route('/note')
def note():
    return render_template('note.html')
