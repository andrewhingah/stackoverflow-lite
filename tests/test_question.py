import json
from .base_test import BaseTestCase


class QuestionsTestCase(BaseTestCase):
        
    def test_post_question(self):
        """Test posting a question."""
        response = self.client.post(
            '/api/v2/questions', data=json.dumps(self.questions), headers=self.authHeaders)

        self.assertEqual(response.status_code, 201)

    def test_get_all_questions(self):
        """Test user view all questions."""
        response = self.client.get(
            '/api/v2/questions', data=json.dumps(self.questions), headers=self.authHeaders)

        self.assertEqual(response.status_code, 200)

    def test_view_single_question(self):
        """Test user view a single question."""
        response = self.client.get(
            '/api/v2/questions/1', data=json.dumps(self.questions), headers=self.authHeaders)

        self.assertEqual(response.status_code, 200)

    def test_edit_question(self):
        """Test user can edit a question."""
        response = self.client.post(
            '/api/v2/questions', data=json.dumps(self.questions), headers=self.authHeaders)
        self.assertEqual(response.status_code, 201)  

        response = self.client.put(
            '/api/v2/questions/1', data=json.dumps(self.questions_1), headers=self.authHeaders)

        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            '/api/v2/questions/1', data=json.dumps(self.questions), headers=self.authHeaders)

        self.assertEqual(response.status_code, 200)

    def test_delete_question(self):
        """Test user can delete a question."""
        response = self.client.get(
            '/api/v2/questions/1', data=json.dumps(self.questions), headers=self.authHeaders)
        
        self.assertEqual(response.status_code, 200)

        response = self.client.delete(
            '/api/v2/questions/1', data=json.dumps(self.questions), headers=self.authHeaders)
        
        self.assertEqual(response.status_code, 200)