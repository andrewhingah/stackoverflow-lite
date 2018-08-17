from flask_api import FlaskAPI
from flask import Flask, jsonify, abort, make_response, request

from instance.config import app_config

def create_app(config_name):

    app = Flask(__name__)


    questions = [
        {
            'id': 1,
            'question': 'What is API?'
        },
        {
            'id': 2,
            'question': 'How to write a simple CRUD API?'
        },
        {
            'id': 3,
            'question': 'Best framework for frontend development'
        },
    ]

    def _get_question(id):
        return [question for question in questions if question['id'] == id]

    @app.errorhandler(400)
    def bad_request(error):
        return make_response(jsonify({'error': "bad request"}), 400)


    @app.route('/api/v1/questions', methods=['GET'])
    def get_questions():
        return jsonify({'questions': questions})

    @app.route('/api/v1/questions/<int:id>', methods=['GET'])
    def get_question(id):
        question = _get_question(id)
        if not question:
            abort(404)
        return jsonify({'questions': question})

    return app

# if __name__ == '__main__':
#     app.run(debug = True)