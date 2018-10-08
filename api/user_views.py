"""This represents user views"""

from flask import Blueprint
from flask_api import FlaskAPI
from flask import request, jsonify, make_response, json, abort
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from datetime import datetime

from api.models import User, Questions, Answer
from api.helpers import insert_user,get_user, get_questions, get_question, edit_question, delete_question

watu = Blueprint("watu", __name__)

@watu.route('/api/v2/auth/signup', methods=['POST'])
def signup():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    user = get_user(email)
    if user is None:
        user = User(name=name,email=email,password=password)
        user.save()
        return jsonify({'message': 'User created!', 'User': user.__dict__})
    else:
        return jsonify({'message':'Email already exists.'})


@watu.route('/api/v2/auth/signin', methods=['POST'])
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