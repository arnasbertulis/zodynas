from flask import Flask

def create_app():
    app = Flask(__name__)
    from website import views
    app.register_blueprint(views.views)
    return app