"""Endpoints are defined here"""

from flask_api import FlaskAPI
from flask import Blueprint
from flask import request, jsonify, make_response, json, abort
from api.models import User, Questions, Answer
from api.helpers import insert_user, get_questions, get_question, edit_question, delete_question

web = Blueprint("web", __name__)

@web.route('/api/v2/auth/signup', methods=['POST'])
def signup():
	user = User(name = request.json.get("name"),
				email = request.json.get("email"),
				username = request.json.get("username"),
				password = request.json.get("password"))
	user.save()
	return jsonify({'message': 'User created!', 'User': user.__dict__})

# @app.route('/api/v2/auth/signin', methods=['POST'])
# def signin():

#     pass

# @app.route('/api/v2/users/questions', methods=['POST'])
# def post_question():

#     pass

# @app.route('/api/v2/questions', methods=['GET'])
# def get_questions():
	
#     pass

# @app.route('/api/v2/questions/<int:id>', methods=['GET'])
# def get_question(id):

#     pass

# @app.route('/api/v2/questions/<int:id>', methods=['PUT'])
# def edit_question(id):

#     pass

# @app.route('/api/v2/questions/<int:id>', methods=['DELETE'])
# def delete_question(id):


#     pass

# @app.route('/api/v2/questions/<int:id>/answers', methods=['POST'])
# def post_answer(id):


#     pass