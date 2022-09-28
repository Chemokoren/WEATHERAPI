import json

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_jwt import utils


class TestViews(TestCase):
    '''
    method runs before any test method
    '''

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('locations-temp', args=['city'])

        self.email = 'test@yoyo.com'
        self.username = 'test'
        self.password = '123456'
        self.user = User.objects.create_user(
            self.username, self.email, self.password)

        self.data = {
            'username': self.username,
            'password': self.password
        }

    '''
    method returns an active access token after a successful login
    '''
    def return_active_token(self):
        client = APIClient(enforce_csrf_checks=True)

        response = client.post('/api/token/', self.data, format='json')
        auth = 'Bearer {0}'.format(response.data['access'])
        return auth

    def test_jwt_login_custom_response_json(self):
        """
        Ensure JWT login view using JSON POST works.
        """
        client = APIClient(enforce_csrf_checks=True)

        response = client.post('/api/token/', self.data, format='json')
        decoded_payload = utils.jwt_decode_handler(response.data['access'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(decoded_payload['user_id'], self.user.id)

    ''' 
    tests if the CityTemperature view accepts args and query_params
    returns 401 if not authenticated, else 200 status code
    '''
    def test_city_temperature(self):
        response = self.client.get(self.list_url, {'number_of_days': 2},HTTP_AUTHORIZATION=self.return_active_token(),format='json')
        self.assertEquals(response.status_code, 200)
