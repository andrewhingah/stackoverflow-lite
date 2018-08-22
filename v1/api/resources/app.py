"""Endpoints are defined here"""

from flask import Flask, jsonify, abort, make_response, request


app = Flask(__name__)

#questions list
quizes = [
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
    return [quiz for quiz in quizes if quiz['id'] == id]

def _record_exists(question):
    return [quiz for quiz in quizes if quiz["question"] == question]

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': "bad request"}), 400)

"""get all questions"""
@app.route('/api/v1/questions', methods=['GET'])
def get_questions():
    return jsonify({'questions': quizes})

"""post a question"""
@app.route('/api/v1/questions', methods=['POST'])
def post_question():
    if not request.json or 'question' not in request.json:
        abort(400)
    question_id = quizes[-1].get("id") + 1
    question = request.json.get('question')
    if _record_exists(question):
        abort(400)

    quiz = {"id": question_id, "question": question,
            "answer": []}
    quizes.append(quiz)
    return jsonify({'question': quiz}), 201

"""get a single question by id"""
@app.route('/api/v1/questions/<int:id>', methods=['GET'])
def get_question(id):
    quiz = _get_question(id)
    if not quiz:
        abort(404)
    return jsonify({'question': quiz})

"""delete a single question by id"""
@app.route('/api/v1/questions/<int:id>', methods=['DELETE'])
def delete_question(id):
    quiz = _get_question(id)
    if len(quiz) == 0:
        abort(404)
    quizes.remove(quiz[0])
    return jsonify({}), 204

"""post an answer to a question by id"""  
@app.route('/api/v1/questions/<int:id>/answer', methods=['POST'])
def post_answer(id):
    quiz = _get_question(id)
    if not quiz:
        abort(404)
    
    answer = request.json.get('answer')
    quiz[0]["answer"].append(answer)

    return jsonify({'questions': quiz}), 201