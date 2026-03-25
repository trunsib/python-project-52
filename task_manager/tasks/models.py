from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.ForeignKey('statuses.Status', on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_tasks')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='executor_tasks')
    labels = models.ManyToManyField('labels.Label', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    