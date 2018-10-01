#api/resources.py
"""Endpoints are defined here"""
from flask import Blueprint
from flask_api import FlaskAPI
from flask import request, jsonify, make_response, json, abort
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from datetime import datetime

from api.models import User, Questions, Answer
from api.helpers import insert_user,get_user, get_questions, get_question, edit_question, delete_question

web = Blueprint("web", __name__)

@web.route('/api/v2/auth/signup', methods=['POST'])
def signup():
	# if user is not None:
 #        return jsonify({'message': "Email already exists."})
	user = User(name = request.json.get("name"),
				email = request.json.get("email"),
				# username = request.json.get("username"),
				password = request.json.get("password"))
	user.save()
	return jsonify({'message': 'User created!', 'User': user.__dict__})


@web.route('/api/v2/auth/signin', methods=['POST'])
def signin():
    email = request.json.get("email")
    password = request.json.get("password")

    user = get_user(email)
    if user is None:
        return jsonify({"message": "user not found"}), 404
    # elif not bcrypt.verify(password, user['password']):
    #     return jsonify({'message': "Incorrect password"}), 400
    else:
        token = create_access_token(identity=request.json.get('email'))
        return jsonify({'message': 'Logged in successfully!', 'token': token})
    return make_response('Your account does not exist!, Please Register!'), 401


@web.route('/api/v2/questions', methods=['POST'])
@jwt_required
def post_question():

    email = get_jwt_identity()
    user = get_user(email)

    question = Questions(
        question = request.json.get("question"),
        date_posted = datetime.now(),
        user_id = (user["id"]))
    question.save()
    return jsonify({'Questions': question.__dict__}), 

@web.route('/api/v2/questions', methods=['GET'])
@jwt_required
def view_all_questions():
    """retrieve all questions"""
    email = get_jwt_identity()
    user = get_user(email)

    # questions = get_questions(user['id']) extra credit feature
    questions = get_questions()
    if questions is None:
    
        return jsonify({'message': 'No questions available'})
    return jsonify({'Questions': questions}), 200

@web.route('/api/v2/questions/<int:id>', methods=['GET'])
@jwt_required
def single_question(id):
    """retrieve single question by id"""
    email = get_jwt_identity()
    user = get_user(email)
    question = get_question(id)
    if question is None:
        return jsonify({'message': 'Question unvailable'})
    return jsonify({'Question': question}), 200

@web.route('/api/v2/questions/<int:id>', methods=['PUT'])
def edit_question(id):
    email = get_jwt_identity()
    user = get_user(email)

    question = Questions(
        question = request.json.get("question"),
        date_posted = datetime.now(),
        user_id = (user["id"]))
    question.save()
    return jsonify({'Question': question}), 201

@web.route('/api/v2/questions/<int:id>', methods=['DELETE'])
@jwt_required
def remove_question(id):
    email = get_jwt_identity()
    user = get_user(email)
    question = get_question(id)
    if question is None:
        return jsonify({"message":"question unvailable"})
    delete_question(id)
    return jsonify({"message":"question has been deleted"}), 200

# @web.route('/api/v2/questions/<int:id>/answers', methods=['POST'])
# def post_answer(id):


#     pass