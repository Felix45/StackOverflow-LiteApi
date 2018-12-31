from app.tests.v1.setup import SetUpTestClient
from app.tests.v1.user_list import *

class UsersModelTest(SetUpTestClient):
	
	def test_get_users(self):
		res = self.client.post("/api/v1/users/list/")
		self.assertEqual(res.status_code, 200)
		
	def test_user_missing_fields(self):
		
		res = self.client.post("/api/v1/users/add/",json=user_0,content_type='application/json')
		self.assertEqual(res.status_code,400)
		self.assertIn('sent an empty request',res.data)
		
		res = self.client.post("/api/v1/users/add/",json=user_1,content_type='application/json')
		self.assertEqual(res.status_code,400)
		self.assertIn('missing required field cpassword from request',res.data)
		
		res = self.client.post("/api/v1/users/add/",json=user_2,content_type='application/json')
		self.assertEqual(res.status_code,400)
		self.assertIn('missing required field email from request',res.data)
		
	def test_blank_values(self):
		
		res = self.client.post("/api/v1/users/add/",json=user_3,content_type='application/json')
		self.assertEqual(res.status_code,400)
		self.assertIn('Field value was empty:',res.data)
		
	def test_is_available(self):
		
		self.client.post("/api/v1/users/add/",json=user_4,content_type='application/json')
		res = self.client.post("/api/v1/users/add/",json=user_5,content_type='application/json')
		self.assertEqual(res.status_code,400)
		self.assertIn('username field value is not available:',res.data)
		
		self.client.post("/api/v1/users/add/",json=user_6,content_type='application/json')
		res = self.client.post("/api/v1/users/add/",json=user_7,content_type='application/json')
		self.assertEqual(res.status_code,400)
		self.assertIn('email field value is not available:',res.data)
		
	def test_is_valid_email(self):
		res = self.client.post("/api/v1/users/add/",json=user_8,content_type='application/json')
		self.assertEqual(res.status_code,400)
		self.assertIn('email is not valid:',res.data)
		
		res = self.client.post("/api/v1/users/add/",json=user_9,content_type='application/json')
		self.assertEqual(res.status_code,400)
		self.assertIn('email is not valid:',res.data)
		
		res = self.client.post("/api/v1/users/add/",json=user_10,content_type='application/json')
		self.assertEqual(res.status_code,200)
		
		
	def test_is_valid_password(self):
		res = self.client.post("/api/v1/users/add/",json=user_11,content_type='application/json')
		self.assertEqual(res.status_code,400)
		self.assertIn('Password should have at least 5 characters, a lowercase, an uppercase and a special character e.g Felix45@ or Emily16#',res.data)
		res = self.client.post("/api/v1/users/add/",json=user_12,content_type='application/json')
		self.assertEqual(res.status_code,400)
		self.assertIn('Password should have at least 5 characters, a lowercase, an uppercase and a special character e.g Felix45@ or Emily16#',res.data)
		res = self.client.post("/api/v1/users/add/",json=user_13,content_type='application/json')
		self.assertEqual(res.status_code,400)
		self.assertIn('Confirm password provided did not match password',res.data)
		res = self.client.post("/api/v1/users/add/",json=user_14,content_type='application/json')
		self.assertEqual(res.status_code,200)
		
	
		
		
		
		
