from flask import Flask
from app.views import init_view
from app.settings import envs
from app.ext import init_ext
def create_app(env):
    
    app=Flask(__name__)
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_view(app)
    return app