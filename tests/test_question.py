"""Module to test the app"""

import unittest
import json

from api.resources import app

BASE_URL = 'http://127.0.0.1:5000/api/v1/questions'
BAD_ITEM_URL = '{}/5'.format(BASE_URL)
GOOD_ITEM_URL = '{}/3'.format(BASE_URL)


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
        self.assertIn(data['question']['question'], 'How to write')
        # cannot add same question again again
        question = {"question": "How to write POST request"}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(question),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        # reset app.questions to initial state
        pass


if __name__ == "__main__":
    unittest.main()