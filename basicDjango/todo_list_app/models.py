from django.db import models
from django.utils import timezone


class todo_list_app(models.Model):
    task = models.CharField(max_length=500)
    due_date = models.DateField(default=timezone.now)
    role = (("HIGH", "HIGH"), ("MEDIUM", "MEDIUM"), ("LOW", "LOW"))
    roles = models.CharField(max_length=10, choices=role, default="default")
