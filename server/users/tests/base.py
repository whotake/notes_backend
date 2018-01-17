from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

User = get_user_model()


class BaseTestCase(APITestCase):

    def setUp(self):
        self.create_user()
        self.api_authentication()

    def create_user(self):
        self.user_data = {
            'username': 'test',
            'email': 'email@email.com',
            'password': 'test',
        }
        self.user = User.objects.create(**self.user_data)

    def api_authentication(self):
        url = reverse('users:api-token-auth')
        response = self.client.post(url, self.user_data, format='json')
        token = response.content.get('token')
        self.set_api_auth_token(token)

    def set_api_auth_token(self, token):
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {token}')
