#coding:utf-8
#文件说明：定义网站视图函数的文件

from app import appweb,db
from flask import render_template,url_for,session,redirect,request,flash
import os.path,time

@appweb.route('/base')
def home():
    return render_template('base.html')


@appweb.route('/project')
@appweb.route('/')
def project():
    return render_template('project.html')


@appweb.route('/article')
def article():
    return render_template('article.html')


@appweb.route('/note')
def note():
    return render_template('note.html')

def imageName():
    imageName = time.strftime('%Y%m%d%H%M%S')
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

#保存文章的视图函数
@appweb.route('/articleUpload',methods=['POST'])
def articleUpload():
    if request.method == 'POST' and request.form['editor1'] is not None:
        article = request.form['editor1']
        article_name = imageName()+'.text'
        article_path = os.path.join(appweb.static_folder,'article',article_name)
        article_file = open(article_path,'w+')
        article_file.write(article.encode('utf-8'))
        article_file.close()
        print('Done')
        return redirect('/base')