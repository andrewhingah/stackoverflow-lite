from flask import Flask, jsonify, abort, make_response, request

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


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': "bad request"}), 400)


@app.route('/api/v1/questions', methods=['GET'])
def get_items():
    return jsonify({'questions': questions})