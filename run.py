"""entry level, run app"""

import os

from api.app import create_app
from api.manage import migrate

config_name = os.getenv('APP_SETTINGS')  # config_name = "development"
app = create_app(config_name)

migrate(app)

if __name__ == '__main__':
    app.run(debug=True)