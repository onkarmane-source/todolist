from django.db import models
import uuid
from django.utils import timezone
from django.core.exceptions import ValidationError


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class ToDoList(models.Model):

    status_choices = [
        ("O", "OPEN"),
        ("W", "WORKING"),
        ("D", "DONE"),
        ("v", "OVERDUE")
    ]

    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    due_date = models.DateField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(
        max_length=2, default="O", choices=status_choices)

    def set_tags(self, x):
        print("xis here", x)
        self.tags = json.dumps(
            list(set((map(lambda a: a.strip(), x.split(","))))))

    def clean(self):
        if self.due_date < timezone.now().date():
            raise ValidationError("Due Date can't be in the Past")

    def get_tags(self):
        return json.loads(self.tags)

    def __str__(self):
        return self.title
