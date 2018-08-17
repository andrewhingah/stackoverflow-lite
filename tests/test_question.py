"""Module to test the app"""

import unittest
import json

from api.resources import app

BASE_URL = 'http://127.0.0.1:5000/api/v1/questions'


class TestStackOverflowApi(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_all(self):
        response = self.app.get('http://127.0.0.1:5000/api/v1/questions')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)

    def test_get_one(self):
        response = self.app.get('http://127.0.0.1:5000/api/v1/questions')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['questions'][0]['question'], 'What is API?')


    def test_post(self):
        
        question = {"question": "How to write POST request"}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(question),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

        data = json.loads(response.get_data())
        self.assertTrue(type(data['question']['id']) is int)
        self.assertIn('How to write', data['question']['question'])

    def test_update_question(self):
        question = {"question": "Best js framework for frontend"}
        response = self.app.put('{}/3'.format(BASE_URL),
                                data=json.dumps(question),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertIn("js", data['question']['question'])

    def test_update_error(self):
        # cannot edit non-existing item
        question = {"question": "How to host an API?"}
        response = self.app.put('{}/5'.format(BASE_URL),
                                data=json.dumps(question),
                                content_type='application/json')
        self.assertEqual(response.status_code, 405)
        
    def test_delete(self):
        response = self.app.delete('{}/3'.format(BASE_URL))
        self.assertEqual(response.status_code, 204)
        response = self.app.delete('{}/5'.format(BASE_URL))
        self.assertEqual(response.status_code, 404)


    def tearDown(self):
        # reset app.questions to initial state
        pass


if __name__ == "__main__":
    unittest.main()