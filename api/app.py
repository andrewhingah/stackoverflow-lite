"""
    This is the core of the app

"""

from flask_api import FlaskAPI
from manage import Database
from api import resources
db = Database()

from instance.config import app_config

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    db.init_app(app)

    return app