import unittest
import json

from api.manage import migrate, clear_migration
from api.app import create_app

class UsersTestCase(unittest.testcase):
	def setUp(self):
		"""Defines test variables and initializes tests """
		self.app = create_app("testing")
		migrate()
		self.checker = self.app.test_client()
		self.users = {'name': 'Samuel Mureithi', 'email': 'mureithi@gmail.com', 'password': 'password'}
		self.default_user = {'name': 'Andrew Hinga', 'email': 'andrewhinga5@gmail.com', 'password': 'password'}
		self.header = {"Content-Type": "application/json"}
		self.checker.post('/api/v2/auth/signup', data=json.dumps(self.default_user), headers=self.header)
	def tearDown(self):
		clear_migration()