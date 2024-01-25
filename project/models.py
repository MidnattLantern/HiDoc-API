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
        return f'{self.id} {self.title}'


class ImageItem(models.Model):
    """
    EXPERIMENTAL
    Image connected to a project.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    for_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image_title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_y8afhe,',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Image for {self.for_project}, by {self.owner}"


class ParagItem(models.Model):
    """
    EXPERIMENTAL
    Paragraph conntected to a project.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    for_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paragraph = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

        def __str__(self):
            return f"Paragraph for {self.for_project}, by {self.owner}"

