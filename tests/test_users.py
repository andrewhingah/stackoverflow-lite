import json
from .base_test import BaseTestCase


class UsersTestCase(BaseTestCase): 
    """This class represents Users."""

        
    def test_signup_user_with_existing_email(self):
        """Test to register user with existing email."""
        data = self.users
        response = self.checker.post('/api/v2/auth/signup', data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEquals(result['message'],'Email already exists.')

    def test_signup_user(self):
        """Test to register new user."""
        data = self.default_user
        response = self.checker.post('/api/v2/auth/signup', data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEquals(result['message'],'User created!')


    def test_signin_user(self):
        """Test user sign in to his/her account."""
        data = self.users
        response = self.checker.post('/api/v2/auth/signin', data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'], "Logged in successfully!")


    def test_signin_user_with_invalid_email_password(self):
        """Test user trying to login with invalid credentials."""
        data = self.default_user
        response = self.checker.post('/api/v2/auth/signin', data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'], "user not found")