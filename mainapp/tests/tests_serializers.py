from rest_framework.test import APITestCase, APIRequestFactory
from mainapp.models import ToDoList, Tag
from mainapp.api.serializers import TaskSerializer


class TaskSerializerTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.request = self.factory.get('/')
        self.request.user = None
        self.tag1 = Tag.objects.create(name="Tag1")
        self.tag2 = Tag.objects.create(name="Tag2")

        self.todo_data = {
            "title": "Test Task",
            "description": "This is a test task.",
            "due_date": "2024-12-31",
            "tags": [self.tag1.name, self.tag2.name],
            "update_tags": ["Tag3", "Tag4"],
            "status": "O",
        }

        self.existing_todo = ToDoList.objects.create(
            title="Existing Task",
            description="Existing description",
            due_date="2024-12-15",
            status="W",
        )
        self.existing_todo.tags.set([self.tag1, self.tag2])

    def test_create_task_with_tags(self):
        serializer = TaskSerializer(data=self.todo_data, context={
                                    "request": self.request})
        self.assertTrue(serializer.is_valid(), serializer.errors)
        task = serializer.save()

        self.assertEqual(task.title, self.todo_data["title"])
        self.assertEqual(task.description, self.todo_data["description"])
        self.assertEqual(task.status, self.todo_data["status"])
        self.assertEqual(task.tags.count(), 4)  # Includes new tags
        self.assertTrue(Tag.objects.filter(name="Tag3").exists())
        self.assertTrue(Tag.objects.filter(name="Tag4").exists())

    def test_update_task_with_tags(self):
        update_data = {
            "title": "Updated Task",
            "description": "Updated description",
            "tags": [self.tag1.name],
            "update_tags": ["Tag5"],
            "status": "D",
        }
        serializer = TaskSerializer(
            instance=self.existing_todo,
            data=update_data,
            partial=True,
            context={"request": self.request},
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        task = serializer.save()

        self.assertEqual(task.title, update_data["title"])
        self.assertEqual(task.description, update_data["description"])
        self.assertEqual(task.status, update_data["status"])
        self.assertEqual(task.tags.count(), 2)  # Tag1 and new Tag5
        self.assertTrue(Tag.objects.filter(name="Tag5").exists())
