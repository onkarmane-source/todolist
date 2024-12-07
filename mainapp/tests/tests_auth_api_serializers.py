from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework import status
from auth.api.serializers import UserSerializer

User = get_user_model()


class UserSerializerTests(APITestCase):

    def setUp(self):
        # sample data
        self.valid_user_data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }
        self.invalid_user_data = {
            'username': 'testuser',
            'password': ''
        }

    def test_create_user_with_valid_data(self):
        serializer = UserSerializer(data=self.valid_user_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertEqual(user.username, self.valid_user_data['username'])
        self.assertTrue(user.check_password(self.valid_user_data['password']))
        self.assertNotEqual(user.password, self.valid_user_data['password'])

    def test_create_user_with_invalid_data(self):
        serializer = UserSerializer(data=self.invalid_user_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)

    def test_create_user_without_password(self):
        data_without_password = {'username': 'newuser'}
        serializer = UserSerializer(data=data_without_password)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)

    def test_create_user_without_username(self):
        data_without_username = {'password': 'password123'}
        serializer = UserSerializer(data=data_without_username)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)

    def test_user_password_is_write_only(self):
        data_with_password = {
            'username': 'newuser',
            'password': 'testpassword123'
        }
        serializer = UserSerializer(data=data_with_password)
        self.assertTrue(serializer.is_valid())

        user = serializer.save()
        serialized_user = UserSerializer(user)
        self.assertNotIn('password', serialized_user.data)

    def test_create_user_with_duplicate_username(self):
        User.objects.create_user(
            username='testuser', password='testpassword123')
        serializer = UserSerializer(data=self.valid_user_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)
