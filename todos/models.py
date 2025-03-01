from django.db import models
from django.db.models import CASCADE

class TodoList(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=CASCADE, related_name="todos")
    # SET_NULL PROTECT DO_NOTHING CASCADE

    def __str__(self):
        return f"{self.title} ({'Done' if self.status else 'Pending'})"
