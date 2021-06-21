from app.settings import BASEDIR
from flask import Blueprint
from flask import render_template,request,flash,session,url_for,redirect,abort
from werkzeug.security import generate_password_hash,check_password_hash
from app.models import Second
import os

second=Blueprint("second",__name__,url_prefix="/bp",template_folder=os.path.join(BASEDIR,"app","templates","second"))



@second.route("/")
def index():
    return render_template("second/index.html")


@second.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        # print("xjkdjkfj")
        return render_template("second/register.html")
    elif request.method=="POST":
        username=request.form.get("username")
        pwd=request.form.get("pwd")
        user=Second()
        user.username=username
        user.pwdhash=pwd #这里到模型中自动格式化为hash值自动保存为pwd
        user.save()
        flash("用户注册成功")
        return render_template('second/secondinfo.html',user=user)

@second.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        if session.get("user"):
            return render_template('second/secondinfo.html',user=Second.query.filter_by(username=session.get("user")).first())
        return render_template("second/login.html")
    elif request.method=="POST":
        username=request.form.get("username")
        pwd=request.form.get("pwd")
        user=Second.query.filter_by(username=username).first()
        if user and user.checkpwd(pwd):
            flash("登录成功")
            session['user']=user.username
            return render_template('second/secondinfo.html',user=user)
            # return redirect(url_for('second.current'))
        flash("用户名或密码错误")
        return render_template("second/login.html")


@second.route("/current")
def current():
    user=session.get("user")
    if user:
        return "当前登录用户是:%s" % user
    return "当前没有登录,请点击<a href='%s'>这里登录</a>" % url_for('first.login')


@second.route("/logout")
def logout():
    session.clear()
    return "退出成功,请点击<a href='%s'>这里登录</a>" % url_for('first.login')



@second.route("/userlist")
def userlist():
    '''登录之后搞个分页'''
    user=session.get("user")
    if user:
        pagination=Second.query.paginate(per_page=2)
        return render_template("second/userlist.html",pagination=pagination)
    else:
        abort(404)