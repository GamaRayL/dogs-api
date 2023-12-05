from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class DogTestCase(APITestCase):
    def setUp(self):
        self.create_url = reverse('main:dog_create')
        self.data = {
            'name': 'Пёс'
        }

        self.user = User.objects.create(
            email='admin@test.com',
            role='admin',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        self.user.set_password('admin')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_post(self):
        response = self.client.post(self.create_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
