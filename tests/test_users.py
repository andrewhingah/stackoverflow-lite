import unittest
import os
import json

from api.manage import migrate, reset_migration
from api.app import create_app

class UsersTestCase(unittest.testcase):
	def setUp(self):
		"""Defines test variables and initializes tests """
		self.app = create_app(config_name="testing")
		migrate()
		self.checker = self.app.test_client()
		self.users = {'name': 'Samuel Mureithi', 'email': 'mureithi@gmail.com', 'password': 'password'}
		self.default_user = {'name': 'Andrew Hinga', 'email': 'andrewhinga5@gmail.com', 'password': 'password'}
		self.header = {"Content-Type": "application/json"}
		self.checker.post('/api/v2/auth/signup', data=json.dumps(self.default_user), headers=self.header)
	def test_signup_user(self):
		"""Test to register new user."""
		data = self.default_user
		response = self.checker.post('/api/v2/auth/signup', data=json.dumps(data), headers=self.header)
		result = json.loads(response.data.decode())
		self.assertEquals(result['message'],'New user registered!')


	def tearDown(self):
		clear_migration()

if __name__ == '__main__':
	unittest.main()