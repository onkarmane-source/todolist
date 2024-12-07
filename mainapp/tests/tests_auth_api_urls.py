from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from mainapp.models import ToDoList, Tag
from django.contrib.auth.models import User


class TestURLs(APITestCase):
    def setUp(self):
        # Create a test user and authenticate
        self.user = User.objects.create_user(
            username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

        # Create a test tag and ToDo item
        self.tag = Tag.objects.create(name="Test Tag")
        self.todo = ToDoList.objects.create(
            title="Test Task",
            description="Test Description",
            due_date="2024-12-31",
        )
        self.todo.tags.add(self.tag)
        self.todo.save()

    def test_list_todos_url(self):
        url = reverse('list-todos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo_url(self):
        url = reverse('create-todo')
        data = {
            "title": "New Task",
            "description": "New Task Description",
            "due_date": "2025-01-01",
            "tags": [self.tag.id],
        }
        response = self.client.post(url, data, format='json')

    def test_detail_todo_url(self):
        url = reverse('detail-todo', kwargs={'pk': self.todo.id})
        response = self.client.get(url)

    def test_update_todo_url(self):
        url = reverse('update-todo', kwargs={'pk': self.todo.id})
        data = {
            "title": "Updated Task",
            "description": "Updated Task Description",
            "due_date": "2025-01-01",
        }
        response = self.client.put(url, data, format='json')

    def test_delete_todo_url(self):
        url = reverse('delete-todo', kwargs={'pk': self.todo.id})
        response = self.client.delete(url)
