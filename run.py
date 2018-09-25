"""entry level, run app"""

import os

from api.app import create_app

config_name = os.getenv('APP_SETTINGS')  # config_name = "development"

app = create_app(config_name)

from api.manage import migrate
migrate()


if __name__ == '__main__':
    app.run(debug=True)