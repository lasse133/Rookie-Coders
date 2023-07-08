from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager
from flask_migrate import Migrate

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Rookie Coders"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    # all routes that are defined in the blueprint of auth/views have the prefix '/'
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Task

    with app.app_context():
        db.create_all()

        tasks = [
            {'title': 'First Task', 'description': 'Insert Personal Data', 'page_name' : 'Part 1'},
            {'title': 'Second Task', 'description': 'Provide Academic Ressources', 'page_name' : 'Part 1'},
            {'title': 'Third Task', 'description': 'Write Letter of Motivation', 'page_name' : 'Part 1'}
        ]

        for task in tasks:
            title = task['title']
            description = task['description']
            page_name = task['page_name']
            new_task = Task(title=title, description=description, page_name=page_name)
            db.session.add(new_task)

        db.session.commit()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app
