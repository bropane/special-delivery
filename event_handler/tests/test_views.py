import json
import pytest

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from .. import views

pytestmark = pytest.mark.django_db


class TestCreateEventView:

    @pytest.fixture
    def user(self):
        return mixer.blend(User)

    @pytest.fixture
    def device(self, user):
        from device_manager.models import Device
        return Device.objects.create(owner=user,
                                     device_id='testID',
                                     name="Test")

    def test_post(self, device, user):
        data = {"device": "testID", "name": "Armed",
                "value": "30", "code": "1", "priority": "3"}
        req = APIRequestFactory().post('/events/update', data, format='json')
        force_authenticate(req, user=user)
        print req.user
        resp = views.CreateEventView.as_view()(req)
        assert resp.status_code == 404, 'Should throw 404 if not found'
