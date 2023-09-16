from django.contrib import admin
from .models import *  # Import the Task model from your models.py file

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at', 'due_date', 'user')
    list_filter = ('completed', 'user')
    search_fields = ('title', 'description', 'user__username')

admin.site.register(Task, TaskAdmin)
