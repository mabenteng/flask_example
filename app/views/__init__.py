from app.views.first import first
from app.views.second import second


def init_view(app):
    app.register_blueprint(first)
    app.register_blueprint(second)