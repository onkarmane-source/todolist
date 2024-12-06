from datetime import datetime
from django.contrib.auth.models import User
from mainapp.models import ToDoList, Tag
from rest_framework import status
from rest_framework.test import APIClient
from mainapp.api.serializers import TagSerializer, TaskSerializer
# from mainapp.models import Tag, ToDoList
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Urgent")

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, "Urgent")
        self.assertEqual(str(self.tag), "Urgent")


class ToDoListModelTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Personal")
        self.valid_due_date = timezone.now().date() + timedelta(days=1)
        self.invalid_due_date = timezone.now().date() - timedelta(days=1)

    def test_todolist_creation(self):
        todo = ToDoList.objects.create(
            title="Finish Django Project",
            description="Complete the Django ToDo app",
            due_date=self.valid_due_date,
        )
        todo.tags.add(self.tag1, self.tag2)

        self.assertEqual(todo.title, "Finish Django Project")
        self.assertEqual(todo.description, "Complete the Django ToDo app")
        self.assertEqual(todo.status, "O")
        self.assertEqual(todo.due_date, self.valid_due_date)
        self.assertIn(self.tag1, todo.tags.all())
        self.assertIn(self.tag2, todo.tags.all())

    def test_todolist_due_date_validation(self):
        with self.assertRaisesMessage(
            ValidationError, "Due Date can't be in the Past"
        ):
            todo = ToDoList(
                title="Past Due Date",
                description="Testing past due date",
                due_date=self.invalid_due_date,
            )
            todo.full_clean()  # Trigger model validation

    def test_todolist_str(self):
        todo = ToDoList.objects.create(
            title="Read a Book",
            description="Read the latest novel",
            due_date=self.valid_due_date,
        )
        self.assertEqual(str(todo), "Read a Book")
