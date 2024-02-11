from django.db import models
from django.contrib.auth.models import User
from project.models import Project


class Documentation(models.Model):
    """
    id automatic by Big Auto.
    Documentation is connected to a post. Hence, the project model.
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
    updated_at = models.DateTimeField(
        auto_now=True
        )
    documentation_title = models.CharField(
        max_length=50, blank=True,
        default='untitled'
        )
    documentation_paragraph = models.TextField(
        blank=True
        )
    documentation_image = models.ImageField(
        upload_to='images/', default='../default_post_y8afhe',
        blank=True,
        )

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.documentation_title
