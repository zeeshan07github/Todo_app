from django.db import models
from django.contrib.auth.models import User  # Import the User model if not already imported

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # Optional task description
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for task creation
    due_date = models.DateTimeField(blank=True, null=True)  # Optional due date for the task
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assign tasks to a user

    def __str__(self):
        return self.title
