# import os
# import django
# import unittest
# from django.test import Client
# from django.contrib.auth import get_user_model
# from myapp.models import Subscription

# # Set up Django environment
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
# django.setup()

# class SaaSTestCase(unittest.TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.User = get_user_model()
#         self.user = self.User.objects.create_user(username='testuser', email='test@example.com', password='password123')
#         self.subscription = Subscription.objects.create(user=self.user, plan='basic')

#     def test_user_login(self):
#         response = self.client.post('/accounts/login/', {'username': 'testuser', 'password': 'password123'})
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('_auth_user_id', self.client.session)
    
#     def test_user_subscription(self):
#         self.assertEqual(self.subscription.plan, 'basic')
    
#     def test_api_access(self):
#         self.client.login(username='testuser', password='password123')
#         response = self.client.get('/api/data/')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('data', response.json())
    
#     def tearDown(self):
#         self.user.delete()
#         self.subscription.delete()

# if __name__ == "__main__":
#     # unittest.main()
message = "hello world"
print(message.replace("hello", " hi"))