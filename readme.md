## flask MTV开发模式样例
### 项目简介
    用来手写一个flask类似django的mtv模式的项目案例,其中包含了数据模型,数据迁移,蓝图,以及功能性的用户注册登录,前端页面美化,数据分页等常用功能,可以用来学习参考当模版使用

### 项目依赖
- Flask                              1.1.4
- Flask-Bootstrap                    3.3.7.1
- Flask-Cache                        0.13.1(老版本,werkzeug版本必须0.12)
- Flask-Caching                      1.10.1
- Flask-Cors                         3.0.10
- Flask-DebugToolbar                 0.11.0
- Flask-Migrate                      2.5.3
- Flask-RESTful                      0.3.8
- Flask-Script                       2.0.6
- Flask-Session                      0.3.2
- Flask-SQLAlchemy                   2.5.1

### 项目路由可访问的地址
    以下是项目路由可用的地址:
!["项目路由可用地址"](/gitimg/route.png)

以下是一些功能页面:
注册页面
!["项目注册页面"](/gitimg/register.png)

比对数据库,登录成功页面
!["项目登录后页面"](/gitimg/userinfo.png)

数据分页的页面

!["数据分页"](/gitimg/userlist.png)


### 项目启动:
    python manage.py runserver -r -d






