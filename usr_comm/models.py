from django.db import models
from django.contrib.auth.models import User
from project.models import Project


class UserComment(models.Model):
    """
    id generated with Big Auto.
    User comment connected to a project.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.comment
