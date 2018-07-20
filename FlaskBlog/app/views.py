#coding:utf-8
#文件说明：定义网站视图函数的文件，服务器启动时执行

from . import appweb,db
from .forms import LoginForm
from .models import User
from flask import render_template,url_for,session,redirect,request,flash
import os.path,time
from flask_login import login_required,login_user,logout_user,current_user
#render_template是python中引入Jinja2模板的库，Jinja2模板引擎方便对html进行更方便的编辑

# @appweb.route('/base')
# def base():
#     return render_template('base.html')

#TODO:目前博客暂时不需要project这个页面
# @appweb.route('/project')
# def project():
#     return render_template('project.html')

@appweb.route('/article',methods=['GET','POST'])
@appweb.route('/')
def article():
    return render_template('article.html')

#--未登录用户禁止访问写文章网页函数--
@appweb.route('/write',methods=['GET','POST'])
@login_required
def writeit():
    return render_template('write.html')

#用户登陆
@appweb.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('article'))
        flash('invalid username or password')
    #--form这个参数使得在forms.py中定义的表单可以传入login.html中--
    return render_template('login.html',form = form)

#用户登出
@appweb.route('/logout')
@login_required
def logout():
    logout_user()
    # flash('You have been logged out')
    return redirect(url_for('article'))

#--用时间戳作为文件名，低访问量下重名几率几乎为零--
def imageName():
    imageName = time.strftime('%Y%m%d%H%M%S')
    return imageName

#--将上传的图片保存--
@appweb.route('/imageUpload',methods = ['POST'])
def imageUpload():
    #回调函数
    if request.method == 'POST' and 'upload' in request.files:
        image = request.files['upload']
        print dir(image)
        image_name = imageName()+'.jpg'
        image_pa = os.path.abspath('uploadImage-cache')
        image_path = os.path.join(appweb.static_folder, 'upload',image_name)
        image.save(image_path)
        #生成图片路径url，供ckeditor回调
        url = url_for('static', filename='%s/%s' % ('upload',image_name))
        callback = request.args.get("CKEditorFuncNum")
        error = ''
        res = """<script type="text/javascript">
                 window.parent.CKEDITOR.tools.callFunction(%s, '%s', '%s');
                 </script>""" % (callback, url, error)
        #window.parent 使得从当前的上传文件的小窗口返回到父类的网页窗口，再选中ckeditor的tools工具栏执行回调
        #用make_response函数将res的js代码包装成一个完整的含html的http响应报文（res部分在html中）
        response = appweb.make_response(res)
        response.headers["Content-Type"] = 'text/html'
        return response

#--将上传的文章保存--
@appweb.route('/articleUpload',methods=['POST'])
def articleUpload():
    if request.method == 'POST' and request.form['editor1'] is not None:
        article = request.values['editor1']#获取文章正文
        article_name = 'text' + imageName()
        article_path = os.path.join(appweb.static_folder,'article',article_name+'.txt')
        article_file = open(article_path,'w+')
        article_file.write(article.encode('utf-8'))
        article_file.close()
        title = request.values['title1']#获取文章标题

        # 为每一篇文章注册地址,由于暂时没有nginx反向代理（主要返回静态网页用）
        # 没有办法保存每篇文章为静态网页，网页内有jinja2引擎生成的部分，为动态网页，需要与后台程序交互
        # 决定为每一篇文章注册地址并把地址保存到数据库
        # 在服务器重启动时全部注册为路由
        articleAdress = '/article/' + article_name
        flash('Upload Article Successful')#在flash中不能用中文，否则decode报错，浏览器会保存flash消息队列依次显示
        return redirect(url_for('writeit'))
    flash('Upload Failed')
    return redirect(url_for('article'))


#iframe需要用到的内嵌网页显示文章的视图函数
@appweb.route('/showArticle',methods=['GET'])
def showArticle():
    return render_template('showArticle.html')