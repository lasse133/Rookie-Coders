from flask import Flask 

def create_app():
    app = Flask(__name__)

    from .views import views
    from .auth import auth

    # all routes that are defined in the blueprint of auth/views have the prefix '/'
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app