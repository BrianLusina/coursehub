from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from usersapi.models import User
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


path = os.getcwd()+"/db.sqlite"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+path
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app