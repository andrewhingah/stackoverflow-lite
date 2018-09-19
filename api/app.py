"""
    This is the core of the app

"""

from flask_api import FlaskAPI
from flask_jwt_extended import JWTManager
from api.database import Database
from flask_cors import CORS

db = Database()
from instance.config import app_config

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    CORS(app)
    # app.config.from_object(app_config['development'])
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    from api import resources

    jwt = JWTManager(app)
    app.register_blueprint(resources.web, url_prefix="/")

    return app