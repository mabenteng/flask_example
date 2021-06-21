from app.func import gettime
from flask.helpers import flash, url_for
from flask import session
from app.ext import cache
from app.models import User, Vip
from flask import Blueprint
from flask import request,render_template,make_response
from flask import redirect
import random,os
from app.ext import db
from flask import g
from werkzeug.security import generate_password_hash,check_password_hash
from app.settings import BASEDIR

first=Blueprint("first",__name__,template_folder=os.path.join(BASEDIR,"app","templates","first"))



@first.route("/")
def index():
    # session["xx"]="ppppp"
    msg=generate_password_hash("pppp")+"<br>"
    msg1=generate_password_hash("pppp")+"<br>"
    msg2=generate_password_hash("pppp")+"<hr>"
    p="pppp"
    res=check_password_hash(msg,p)
    res1=check_password_hash(msg1,p)
    res2=check_password_hash(msg2,p)
    print(res)
    print(res1)
    print(res2)
    return "i am flaske  <hr>%s" % msg+msg1+msg2



@first.route("/adduser",methods=["GET","POST"])
def adduser():
    if request.method=="GET":
        return render_template("adduser.html")
    elif request.method=="POST":
        name=request.form.get("username")
        addr=request.form.get("addr")
        age=request.form.get("age")
        user=User()
        user.name=name
        user.addr=addr
        user.age=age
        user.save()
        # flash("数据添加成功")#在模版中配合get_flashed_messages()迭代器用
        # g.msg="helloworld!!!",只能在本模版路由中使用g的变量
        session["user"]="daoxiangshiwo"
        return redirect(url_for("first.userlist"))

# 搞一个批量添加用户的
@first.route("/addusers")
def addusers():
    #就get访问批量添加
    for i in range(20):
        c="小白用户%d" % random.randrange(999999)
        d="城市%d" % random.randrange(39)
        e=random.randint(18,60)
        user=User(name=c,addr=d,age=e)
        db.session.add(user)
    db.session.commit() 
    return "批量添加了20个用户"

@first.route("/userlist")
# @cache.cached(timeout=60)
def userlist():
    #这里也要考虑分页
    # page=request.args.get("page",1,type=int)#分页默认值为int,paginate内会自动获取get参数[page和per_page]
    # per_page=request.values.get("per_page",4,type=int)
    pagination=User.query.paginate()
    # g.msg="userlist的大g,不用在模版传递也可以使用很方便"
    # g.msg=session["user"]
    print(pagination)
    print("我是userlist函数执行过程")
    # print(gettime())#这里调用的是缓存函数,过期20s
    return render_template("userlist.html",pagination=pagination)




@first.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    elif request.method=="POST":
        username=request.form.get("username")
        pwd=request.form.get("pwd")
        user=Vip()
        user.username=username
        user.pwd=generate_password_hash(pwd)
        user.save()
        flash("用户注册成功")
        return render_template('vipinfo.html',user=user)

@first.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method=="POST":
        username=request.form.get("username")
        pwd=request.form.get("pwd")
        user=Vip.query.filter_by(username=username).first()
        if user and check_password_hash(user.pwd,pwd):
            flash("登录成功")
            session['user']=user.username
            return render_template('vipinfo.html',user=user)
        flash("用户名或密码错误")
        return render_template("login.html")


@first.route("/current")
def current():
    user=session.get("user")
    if user:
        return "当前登录用户是:%s" % user
    return "当前没有登录,请点击<a href='%s'>这里登录</a>" % url_for('first.login')


@first.route("/logout")
def logout():
    session.clear()
    return "退出成功,请点击<a href='%s'>这里登录</a>" % url_for('first.login')


@first.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")



