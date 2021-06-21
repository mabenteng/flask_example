from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# 搞个debug工具条
from flask_debugtoolbar import DebugToolbarExtension
# 搞个缓存需要用flask_caching这个版本不会报错
from flask_caching import Cache
# 前端bootstrap和flask的结合静态库
from flask_bootstrap import Bootstrap

db=SQLAlchemy()
migrate=Migrate()
toolbar=DebugToolbarExtension()#先创建工具栏空对象之后懒加载
cache=Cache()

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app,db)
    toolbar.init_app(app)
    cache.init_app(app,config={'CACHE_TYPE':'filesystem','CACHE_DIR':"./tmp"})
    Bootstrap(app)

