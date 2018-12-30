from app.tests.v1.setup import SetUpTestClient

class UsersModelTest(SetUpTestClient):
	
	def test_get_users(self):
		res = self.client.post("/api/v1/users/list/")
		self.assertEqual(res.status_code, 400)
		
