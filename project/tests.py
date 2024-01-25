from django.contrib.auth.models import User
from .models import Project
from rest_framework import status
from rest_framework.test import APITestCase


class ProjectListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='cherry', password='berrybasket')

    def test_can_list_project(self):
        testuser1 = User.objects.get(username='cherry')
        Project.objects.create(owner=testuser1, project_title='on top')
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_in_user_can_create_project(self):
        self.client.login(username='cherry', password='berrybasket')
        response = self.client.post('/projects/', {'title': 'on top'})
        count = Project.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logout_user_cant_create_project(self):
        response = self.client.post('/projects/', {'title': 'on top'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)