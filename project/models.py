from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """
    id is automatically generated with Big Auto.
    Conntected to an artist.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_title = models.CharField(max_length=50, blank=True)
    project_description = models.TextField(blank=True)
    feature_poster = models.ImageField(
        upload_to='images/', default='../default_post_y8afhe,',
        blank=True,
    )
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f'{self.id} {self.project_title}'
