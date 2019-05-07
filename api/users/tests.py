from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserTest(APITestCase):
    def test_create_user_success(self):
        test_case = [
            {
                "username" : "gwangd",
                "email"    : "gwangyonglee92@gmail.com",
                "password" : "qwe123"
            }
        ]
        for i in test_case:
            res = self.client.post('/api/v1/users/', data=i)
            self.assertEquals(res.status_code, status.HTTP_201_CREATED)