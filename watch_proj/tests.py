from django.contrib.auth.models import User
from .models import WatchProject
from .models import Project
from rest_framework import status
from rest_framework.test import APITestCase


class WatchProjectViewTest(APITestCase):
    def setUp(self):
        testuser1 = User.objects.create_user(
            username='cherry', password='berrybasket'
        )
        testuser2 = User.objects.create_user(
            username='crispy', password='nachos'
        )
        Project.objects.create(
            owner=testuser1, project_title='on top'
            )
        WatchProject.objects.create(
            owner=testuser2, project='on top'
        )
