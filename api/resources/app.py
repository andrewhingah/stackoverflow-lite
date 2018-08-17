# from flask_api import FlaskAPI
from flask import Flask, jsonify, abort, make_response, request

# from instance.config import app_config

# def create_app(config_name):

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

def _record_exists(question):
    return [question for question in questions if question["question"] == question]

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

@app.route('/api/v1/questions', methods=['POST'])
def post_question():
    if not request.json or 'question' not in request.json:
        abort(400)
    question_id = questions[-1].get("id") + 1
    question = request.json.get('question')
    if _record_exists(question):
        abort(400)
    question = {"id": question_id, "question": question}
    questions.append(question)
    return jsonify({'question': question}), 201
