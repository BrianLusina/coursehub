from flask import Flask
from . import bootstrap
import os

path = os.getcwd()+"/db.sqlite"

def create_course_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+path

    database_url = (
        "postgresql://sanctumlabs:sanctumlabs@localhost:5432/sanctumlabs_dbkit-sql"
    )
    
    bootstrap(database_url='sqlite:///'+path)

    from .routes import routes as route_blueprint
    app.register_blueprint(route_blueprint)
    return app
