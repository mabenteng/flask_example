# flask MTV开发模式样例
## 项目简介

用来手写一个flask类似django的mtv模式的项目案例,其中包含了数据模型,数据迁移,蓝图,以及功能性的用户注册登录,前端页面美化,数据分页等常用功能,可以用来学习参考当模版使用,掌握这些基本就可以一点一点开发比较复杂的系统了.

## 项目依赖
- Flask                              1.1.4 flask框架>0.8
- Flask-Bootstrap                   3.3.7.1前端模版调用bootstrap
- Flask-Cache缓存            0.13.1(老版本不更新了,werkzeug版本必须0.12,否则不兼容)
- Flask-Caching                      1.10.1 (可以安装这个替代flask-cache,不存在兼容性问题)
- Flask-Cors                         3.0.10 用来跨域用,本项目没有使用
- Flask-DebugToolbar                 0.11.0 类似django的debug工具条
- Flask-Migrate                      2.5.3用来生成迁移文件配合flask_script命令使用
- Flask-RESTful                      0.3.8 前后端分离的restful接口调用
- Flask-Script                       2.0.6 将flask改造成类django命令行启动
- Flask-Session                      0.3.2 改造原生session可以保存redis/文件系统等方式
- Flask-SQLAlchemy                   2.5.1 flask的ORM关系模型映射

## 项目目录
- app项目核心目录
    - templates模版目录
    - views视图函数目录
    - \_\_init__.py 定义create_app创建flask函数
    - ext.py 第三方扩展库 模型,迁移,缓存,Debug工具条,bootstrap等等
    - func.py 公共函数文件
    - models.py 用户自定义模型文件
    - settings.py 项目配置文件
- manage.py 项目入口文件
- tmp 这个是flask-caching缓存保存目录,可以删除
- migrations 数据迁移目录,可以删除
- gitimg git引用图片目录,可以删除

可以clone到本地查看源码实现过程


## 项目路由可访问的地址
    以下是项目路由可用的地址:
    second蓝图路由[/bp/*]引入了前端bootstrap,其他没有
!["项目路由可用地址"](/gitimg/route.png)

    以下是一些功能页面:
注册页面
!["项目注册页面"](/gitimg/register.png)

    比对数据库,登录成功页面
!["项目登录后页面"](/gitimg/userinfo.png)

    数据分页的页面

!["数据分页"](/gitimg/userlist.png)


## 项目启动:
    python manage.py runserver -r -d

## 其他信息
后续会更新相关flask学习笔记的Xmind思维导图总结,想要了解更多的信息,请移步到[这里](https://github.com/mabenteng/it-xmind )




