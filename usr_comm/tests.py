from django.contrib.auth.models import User
from .models import UserComment
from project.models import Project
from rest_framework import status
from rest_framework.test import APITestCase


class UserCommentViewTests(APITestCase):
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

    def test_retrieve_valid_project(self):
        response = self.client.get('/projects/1/')
        self.assertEqual(response.data['project_title'], 'fruitsallad')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # failed
    def test_comment_valid_project(self):
        response = self.client.get('/projects/1/')
        self.assertEqual(response.data['project_title'], 'fruitsallad')
        self.assertEqual(response.data['comment'], 'berries belong here too')
        self.assertEqual(response.status_code, status.HTTP_200_OK)