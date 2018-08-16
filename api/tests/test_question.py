"""Module to test the app"""

import unittest
import json

from app.resources import questions


class TestStackOverflowApi(unittest.TestCase):

    def setUp(self):
        self.app = questions.app.test_client()
        self.app.testing = True

    def test_get_all(self):
        response = self.app.get('http://127.0.0.1:5000/api/v1/questions')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        # reset app.questions to initial state
        pass


if __name__ == "__main__":
    unittest.main()