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
        response = self.client.post('/projects/', {'project_title': 'on top'})
        count = Project.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logout_user_cant_create_project(self):
        response = self.client.post('/projects/', {'project_title': 'on top'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ProjectDetailViewTests(APITestCase):
    def setUp(self):
        testuser1 = User.objects.create_user(
            username='cherry', password='berrybasket'
        )
        testuser2 = User.objects.create_user(
            username='crispy', password='nachos'
        )
        Project.objects.create(
            owner=testuser1, project_title='fruitsallad',
            project_description='berries belong in fruitsallads'
        )
        Project.objects.create(
            owner=testuser2, project_title='frying',
            project_description='how to make anything crispy'
        )

    def test_can_retrieve_valid_id(self):
        response = self.client.get('/projects/1/')
        self.assertEqual(response.data['project_title'], 'fruitsallad')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_invalid_id(self):
        response = self.client.get('/posts/9')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_owner_can_update_post(self):
        self.client.login(username='cherry', password='berrybasket')
        response = self.client.put(
            '/projects/1/', {'project_title': 'on sundae'}
        )
        project = Project.objects.filter(pk=1).first()
        self.assertEqual(project.project_title, 'on sundae')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_another_post(self):
        self.client.login(username='cherry', password='berrybasket')
        response = self.client.put(
            '/projects/2/', {'project_title': 'on sundae'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
