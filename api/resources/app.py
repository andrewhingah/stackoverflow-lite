"""Endpoints are defined here"""

from flask import Flask, jsonify, abort, make_response, request


app = Flask(__name__)

#questions list
questions = [
    {
        'id': 1,
        'question': 'What is API?',
        'answer':[]
    },
    {
        'id': 2,
        'question': 'How to write a simple CRUD API?',
        'answer':[]
    },
    {
        'id': 3,
        'question': 'Best framework for frontend development',
        'answer':[]
    },
]

def _get_question(id):
    return [question for question in questions if question['id'] == id]

def _record_exists(question):
    return [question for question in questions if question["question"] == question]

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': "bad request"}), 400)

"""get all questions"""
@app.route('/api/v1/questions', methods=['GET'])
def get_questions():
    return jsonify({'questions': questions})

"""post a question"""
@app.route('/api/v1/questions', methods=['POST'])
def post_question():
    if not request.json or 'question' not in request.json:
        abort(400)
    question_id = questions[-1].get("id") + 1
    question = request.json.get('question')
    if _record_exists(question):
        abort(400)
    question = {"id": question_id, "question": question, "answer":[]}
    questions.append(question)
    return jsonify({'question': question}), 201

"""get a single question by id"""
@app.route('/api/v1/questions/<int:id>', methods=['GET'])
def get_question(id):
    question = _get_question(id)
    if not question:
        abort(404)
    return jsonify({'questions': question})

"""delete a single question by id"""
@app.route('/api/v1/questions/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = _get_question(id)
    if len(question) == 0:
        abort(404)
    questions.remove(question[0])
    return jsonify({}), 204

"""post an answer to a question by id"""  
@app.route('/api/v1/questions/answer/<int:id>', methods=['POST'])
def post_answer(id):
    question = _get_question(id)
    
    answer = request.json.get('answer')
    question[0]["answer"].append(answer)

    return jsonify({'questions': question}), 201