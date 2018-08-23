"""Endpoints are defined here"""

from flask_api import FlaskAPI

from api.models import User, Questions, Answer

app = FlaskAPI(__name__, instance_relative_config=True)

@app.route('/api/v2/auth/signup', methods=['POST'])
def signup():
	"""
	signs up a new user
	"""

    pass

@app.route('/api/v2/auth/signin', methods=['POST'])
def signin():
	"""
	logs in a registered user
	"""

    pass

@app.route('/api/v2/users/questions', methods=['POST'])
def post_question():
	"""
	posts a new question
	"""

    pass

@app.route('/api/v2/questions', methods=['GET'])
def get_questions():
	"""
	fetches all questions
	"""

    pass

@app.route('/api/v2/questions/<int:id>', methods=['GET'])
def get_question(id):
	"""
	gets single question by id
	"""

    pass

@app.route('/api/v2/questions/<int:id>', methods=['PUT'])
def edit_question(id):
	"""
	updates a question
	"""

    pass

@app.route('/api/v2/questions/<int:id>', methods=['DELETE'])
def delete_question(id):
	"""
	deletes a question by id

	"""

    pass

@app.route('/api/v2/questions/<int:id>/answers', methods=['POST'])
def post_answer(id):
	"""
	posts an answer to a question
	"""

    pass