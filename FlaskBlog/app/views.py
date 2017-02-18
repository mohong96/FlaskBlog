#coding:utf-8
#文件说明：定义网站视图函数的文件，服务器启动时执行

from . import appweb,db
from flask import render_template,url_for,session,redirect,request,flash
import os.path,time

@appweb.route('/base')
def base():
    return render_template('base.html')

@appweb.route('/home')
def home():
    return render_template('home.html')

@appweb.route('/project')
@appweb.route('/')
def project():
    return render_template('project.html')


@appweb.route('/article')
def article():
    return render_template('article.html')


def imageName():
    imageName = time.strftime('%Y%m%d')
    return imageName
@appweb.route('/imageUpload',methods = ['POST'])
def imageUpload():
    #回调函数
    url = ''
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

#保存文章为TXT文件
@appweb.route('/articleUpload',methods=['POST'])
def articleUpload():
    if request.method == 'POST' and request.form['editor1'] is not None:
        article = request.values['editor1']
        article_name = imageName()
        article_path = os.path.join(appweb.static_folder,'article',article_name+'.txt')
        article_file = open(article_path,'w+')
        article_file.write(article.encode('utf-8'))
        article_file.close()
        # 为每一篇文章注册地址,由于暂时没有nginx反向代理（主要返回静态网页用）
        # 没有办法保存每篇文章为静态网页，网页内有jinja2引擎生成的部分，为动态网页，需要与后台程序交互
        # 决定为每一篇文章注册地址并把地址保存到数据库
        # 在服务器重启动时全部注册为路由
        articleAdress = '/article/' + article_name
        articleAdress.
        return redirect('/base')


#iframe需要用到的内嵌网页显示文章的视图函数
@appweb.route('/showArticle',methods=['GET'])
def showArticle():
    return render_template('showArticle.html')