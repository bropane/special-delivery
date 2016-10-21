import json
import pytest

from rest_framework.test import APIRequestFactory
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from .. import views

pytestmark = pytest.mark.django_db


class TestUpdateLocationView:

    def test_post(self):
        req = APIRequestFactory().post('/location/update', {"position": "33.456734,-144.450985", "coreid": "testID"}, format='json')
        resp = views.CreateEventView.as_view()(req)
        assert resp.status_code == 404, 'Should throw 404 if not found'
