from django.db import models

class Task(models.Model):

    completed = models.BooleanField(default=False)
    description = models.CharField(max_length=255, blank=False)