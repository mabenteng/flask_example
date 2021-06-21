from datetime import datetime
from app.ext import cache

'''
一个flask库经常使用封装的函数,

'''
@cache.cached(timeout=20,key_prefix="gettime")
def gettime():
    print("我是没有缓存的gettime()函数")
    return datetime.now()