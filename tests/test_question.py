# """
#     Test cases for the 
#     various endpoints
# """

# from copy import deepcopy
# import unittest
# import json

# from api.resources import app

# QUIZ_URL = 'http://127.0.0.1:5000/api/v1/questions'


# class TestStackOverflowApi(unittest.TestCase):

#     """
#         Runs before every test.
#         Backs up the questions dictionary
#     """

#     def setUp(self):
#         self.backup_quizes = deepcopy(app.quizes)
#         self.app = app.app.test_client()
#         self.app.testing = True

#     def test_get_all(self):
#         """
#             Test fetch all questions
#         """
#         response = self.app.get(QUIZ_URL)
#         data = json.loads(response.get_data())
#         self.assertEqual(response.status_code, 200)


#     def test_get_one(self):
#         """
#         Tests if a question can be retrieved by id
#         """
#         response = self.app.get('{}/1'.format(QUIZ_URL))
#         data = json.loads(response.get_data())
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('What is API?',data['question'][0]['question'])
#         self.assertEqual(data['question'][0]['id'],1)

#     def test_post(self):
#         """
#         Test if one can post a new question
#         If question already exists, test status_code is 400
#         """
        
#         question = {"question": "How to write POST request"}
#         response = self.app.post(QUIZ_URL,
#                                  data=json.dumps(question),
#                                  content_type='application/json')
#         self.assertEqual(response.status_code, 201)

#         data = json.loads(response.get_data())
#         self.assertTrue(type(data['question']['id']) is int)
#         self.assertIn('How to write', data['question']['question'])

#         #test user cannot post a question that
#         #already exists

#         question = {"question": "How to write POST request"}
#         response = self.app.post(QUIZ_URL,
#                                  data=json.dumps(question),
#                                  content_type='application/json')
#         self.assertEqual(response.status_code, 400)

#     def test_delete(self):
#         """
#         Test a question can be deleted given id
#         If id doesn't exist, test status_code is 404
#         """
#         response = self.app.get('{}/3'.format(QUIZ_URL))
#         self.assertEqual(response.status_code, 200)
#         response = self.app.delete('{}/3'.format(QUIZ_URL))
#         self.assertEqual(response.status_code, 204)
#         #test a deleted item cannot be accessed
#         response = self.app.get('{}/3'.format(QUIZ_URL))
#         self.assertEqual(response.status_code, 404)
#         response = self.app.delete('{}/3'.format(QUIZ_URL))
#         self.assertEqual(response.status_code, 404)

#     def test_post_answer(self):
#         """
#         Test user can post an answer to a question given id
#         If id doesn't exist, test status_code is 404
#         """
    
#         answer = {"answer": "lorem ipsum"}
#         response = self.app.post('{}/1/answer'.format(QUIZ_URL),
#                                  data=json.dumps(answer),
#                                  content_type='application/json')
#         self.assertEqual(response.status_code, 201)

#         #test user can't post answer to unexisting id
#         answer = {"answer": "lorem ipsum"}
#         response = self.app.post('{}/1000/answer'.format(QUIZ_URL),
#                                  data=json.dumps(answer),
#                                  content_type='application/json')
#         self.assertEqual(response.status_code, 404)

#     def test_edit_question(self):
#         """
#         test that user can edit a question.
#         if question doesn't exist, add to the list
#         """
#         question = {"question": "What API's does google have?"}
#         response = self.app.put('{}/1'.format(QUIZ_URL),
#                                 data=json.dumps(question),
#                                 content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         data = json.loads(response.get_data())
#         self.assertEqual(data['question']['question'], "What API's does google have?")


#     def tearDown(self):
#         """
#         reset app.questions to initial state
#         """
#         app.quizes = self.backup_quizes


# if __name__ == "__main__":
#     unittest.main()