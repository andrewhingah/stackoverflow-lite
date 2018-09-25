""" Base test cases for the API endpoints."""
import unittest 
import os
import json


from api.manage import migrate, reset_migration

from api.app import create_app

class BaseTestCase(unittest.TestCase):
    """This class represent Users, Questions."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        migrate()

        self.checker = self.app.test_client()
        self.users = {'name': 'Andrew Hinga', 'email': 'andrewhinga5@gmail.com', 'password': 'password'}
        self.default_user = {'name': 'John Lewis', 'email': 'john@gmail.com', 'password': '1881'} 
    
        self.client = self.app.test_client()
        self.questions = {'question': 'How to structure css?'}
        self.questions_1 = {'question': 'What is an API?'}


        self.user = {'name': 'Andrew Hinga', 'email': 'andrewhinga5@gmail.com', 'password': 'password'}
        self.header = {"Content-Type": "application/json"}
        
        # create an authenticated user
        self.client.post('/api/v2/auth/signup', data=json.dumps(self.user), headers=self.header)

        # login the user
        response = self.client.post("/api/v2/auth/signin", data=json.dumps(self.user), headers=self.header)

        # create the authentication headers
        self.authHeaders = {"Content-Type":"application/json"}

        # fix the bearer token in the header
        result = json.loads(response.data.decode())
        self.authHeaders['Authorization'] = 'Bearer '+result['token']



    def tearDown(self):
        reset_migration()

if __name__ == "__main__":
    unittest.main()