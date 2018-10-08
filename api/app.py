"""
    This is the core of the app

"""
from flask_api import FlaskAPI
from flask_jwt_extended import JWTManager
from api.database import Database

db = Database()
from instance.config import app_config

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    
    
    # app.config.from_object(app_config['development'])
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    jwt = JWTManager(app)

    from api import user_views, questions_views

    app.register_blueprint(user_views.watu, url_prefix="/")
    app.register_blueprint(questions_views.questions, url_prefix="/")

    return app