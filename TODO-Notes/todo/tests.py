import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from .views import ToDoModelViewSet
from .models import Project
from users.models import User as ToDoUser
from django.contrib.auth.models import User, Permission
from mixer.backend.django import mixer


class TestToDoViewSet(TestCase):

    def test_get_list_auth(self):
        factory = APIRequestFactory()
        user = User.objects.create_user('developer', 'hanna@develops.com', 'hannadevelops')
        request = factory.get('/todo')
        force_authenticate(request, user)
        view = ToDoModelViewSet.as_view({'get':'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUserViewSet(TestCase):

    def test_get_detail_guest(self):
        user = ToDoUser.objects.create(username='Paul', firstname='Paul', lastname='Moses', birth_date='1981-08-11', email='paul@home.com')
        client = APIClient()
        response = client.get(f'/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestProjectViewSet(APITestCase):

    def test_delete_admin(self):
        user = ToDoUser.objects.create(username='Paul', firstname='Paul', lastname='Moses', birth_date='1981-08-11', email='paul@home.com')
        project = Project.objects.create(name='Electronic store', link_to_repo='a_link')
        project.user.add(user)
        project.save()
        admin = User.objects.create_user('Andy', 'andyadmin@develops.com', 'andyadmin')
        permission_project_view = Permission.objects.get(codename='view_project')
        permission_project_delete = Permission.objects.get(codename='delete_project')
        admin.user_permissions.add(permission_project_view, permission_project_delete)
        admin.save()
        self.client.login(username='Andy', password='andyadmin')
        response = self.client.delete(f'/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f'/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.client.logout()


    def test_delete_admin_with_mixer(self):
        project = mixer.blend(Project)
        admin = User.objects.create_user('Andy', 'andyadmin@develops.com', 'andyadmin')
        permission_project_view = Permission.objects.get(codename='view_project')
        permission_project_delete = Permission.objects.get(codename='delete_project')
        admin.user_permissions.add(permission_project_view, permission_project_delete)
        admin.save()
        self.client.login(username='Andy', password='andyadmin')
        response = self.client.delete(f'/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f'/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.client.logout()
