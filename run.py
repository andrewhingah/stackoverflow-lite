"""entry level, run app"""

from api.resources.app import app

if __name__ == '__main__':
    app.run(debug=True)