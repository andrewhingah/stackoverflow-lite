"""This is the questions views"""

from flask import Blueprint
from flask_api import FlaskAPI
from flask import request, jsonify, make_response, json, abort
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from datetime import datetime

from api.models import User, Questions, Answer
from api.helpers import insert_user,get_user, get_questions, get_question, edit_question, delete_question

questions = Blueprint("questions", __name__)


@questions.route('/api/v2/questions', methods=['POST'])
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

@questions.route('/api/v2/questions', methods=['GET'])
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

@questions.route('/api/v2/questions/<int:id>', methods=['GET'])
@jwt_required
def single_question(id):
    """retrieve single question by id"""
    email = get_jwt_identity()
    user = get_user(email)
    question = get_question(id)
    if question is None:
        return jsonify({'message': 'Question unvailable'})
    return jsonify({'Question': question}), 200

@questions.route('/api/v2/questions/<int:id>', methods=['PUT'])
@jwt_required
def update_question(id):
    email = get_jwt_identity()
    user = get_user(email)

    quest_to_be_edited = get_question(id)
    if quest_to_be_edited is None:
        question = Questions(
            question = request.json.get("question"),
            date_posted = datetime.now(),
            id = id,
            user_id = (user["id"]))
        question.save()

        return jsonify({'Question': question.__dict__,
            'message': "New question created"}),

    else:
        quest_to_be_edited['question'] = request.json.get('question')
        quest_to_be_edited['date_posted'] = datetime.now()
        edit_question(id, quest_to_be_edited)

        return jsonify({"Question":quest_to_be_edited,
            "message":"Updated successfully"}), 200


@questions.route('/api/v2/questions/<int:id>', methods=['DELETE'])
@jwt_required
def remove_question(id):
    email = get_jwt_identity()
    user = get_user(email)
    question = get_question(id)
    if question is None:
        return jsonify({"message":"question unvailable"})
    delete_question(id)
    return jsonify({"message":"question has been deleted"}), 200

@questions.route('/api/v2/questions/<int:id>/answers', methods=['POST'])
@jwt_required
def post_answer(id):
    email = get_jwt_identity()
    user = get_user(email)
    question = get_question(id)
    if question is None:
        return jsonify({"message":"question unvailable"})
    answer = Answer(
        answer = request.json.get("answer"),
        date_posted = datetime.now(),
        question_id = (question["id"]))
    answer.save()
    return jsonify({'message':'your answer has been posted'})