"""models"""
from api import helpers

class User(object):
    """
    User class

    """

    def __init__(self, id=0, name="", email="", username="", password=""):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.username = username

    def save(self):
        helpers.insert_user(self)

    def addUser(self):
        pass

class Questions(object):
    """
    Questions class
    """

    def __init__(self, id=0, question="", date_posted="", user_id=""):
        self.id = id
        self.question = question
        self.date_posted = date_posted
        self.user_id = user_id

    def save(self):
        helpers.create_question(self)


class Answer(object):
    """
    Answers class
    """

    def __init__(self, id=0, answer="", date_posted="", question_id=""):
        self.id = id
        self.answer = answer
        self.date_posted = date_posted
        self.question_id = question_id
        
    def save(self):
        pass