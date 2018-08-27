"""
    This is the core of the app

"""

from flask_api import FlaskAPI
from flask_jwt_extended import JWTManager
from instance.config import app_config

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    from api import resources

    jwt = JWTManager(app)
    app.register_blueprint(resources.web, url_prefix="/")

    return app