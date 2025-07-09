from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "strongpassword123",
            "password2": "strongpassword123"
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="testuser").exists())
