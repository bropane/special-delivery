import pytest

from rest_framework.test import APIClient
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .. import views

pytestmark = pytest.mark.django_db


class TestCreateEventView:

    @pytest.fixture
    def user_owner(self):
        return User.objects.create(email='test@email.com',
                                   password='test',
                                   username='I Own the Test Device')

    @pytest.fixture
    def user(self):
        return User.objects.create(email='test2@email.com',
                                   password='test',
                                   username='I am a random user')

    @pytest.fixture
    def device(self, user_owner):
        from device_manager.models import Device
        return Device.objects.create(owner=user_owner,
                                     device_id='testID',
                                     name="Test")

    @pytest.fixture
    def data(self):
        return {"device": "testID", "name": "Armed",
                "value": "30", "code": "1", "priority": "3"}

    def test_no_device_exists(self, data, user_owner):
        token = Token.objects.get(user__username=user_owner.username)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.post('/events/update', data, format='json')
        assert response.status_code == 404, ("Should NOT post successfully, "
                                             "No Device Exists")

    def test_authenticated_post(self, device, user_owner, data):
        token = Token.objects.get(user__username=user_owner.username)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.post('/events/update', data, format='json')
        assert response.status_code == 201, "Should post successfully"

    def test_unauthenticated_post(self, device, data):
        client = APIClient()
        response = client.post('/events/update', data, format='json')
        assert response.status_code == 403, ("Should NOT post successfully, "
                                             "Unauthenticated")

    def test_unauthorized_post(self, device, user, data):
        token = Token.objects.get(user__username=user.username)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.post('/events/update', data, format='json')
        assert response.status_code == 403, ("Should NOT post successfully "
                                             "Not Authorized")
