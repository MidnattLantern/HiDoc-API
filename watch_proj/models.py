from django.db import models
from django.contrib.auth.models import User
from project.models import Project


class WatchProject(models.Model):
    """
    id is automatically generated with Big Auto.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'project',]

    def __str__(self):
        return f'{self.owner} {self.project}'
