"""
    Test cases for the 
    various endpoints
"""

from copy import deepcopy
import unittest
import json

from api.resources import app

QUIZ_URL = 'http://127.0.0.1:5000/api/v1/questions'


class TestStackOverflowApi(unittest.TestCase):

    def setUp(self):
        self.backup_questions = deepcopy(app.questions)
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_all(self):
        response = self.app.get(QUIZ_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)

    def test_get_one(self):
        response = self.app.get(QUIZ_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['questions'][0]['question'], 'What is API?')


    def test_post(self):
        
        question = {"question": "How to write POST request"}
        response = self.app.post(QUIZ_URL,
                                 data=json.dumps(question),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

        data = json.loads(response.get_data())
        self.assertTrue(type(data['question']['id']) is int)
        self.assertIn('How to write', data['question']['question'])

    def test_delete(self):
        response = self.app.delete('{}/3'.format(QUIZ_URL))
        self.assertEqual(response.status_code, 204)
        response = self.app.delete('{}/5'.format(QUIZ_URL))
        self.assertEqual(response.status_code, 404)

    def test_post_answer(self):
    
        answer = {"answer": "lorem ipsum"}
        response = self.app.post('{}/1/answer'.format(QUIZ_URL),
                                 data=json.dumps(answer),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)


    def tearDown(self):
        # reset app.questions to initial state
        app.questions = self.backup_questions


if __name__ == "__main__":
    unittest.main()