import json
import pytest

from rest_framework.test import APIRequestFactory
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from .. import views

pytestmark = pytest.mark.django_db


class TestCreateEventView:

    def test_post(self):
<<<<<<< HEAD
        data = json.dumps({"name": "BATTLOW", "code": 1, "priority": 3})
        req = APIRequestFactory().post('/events/update', {"data": data, "coreid": "testID", "name": "BATTLOW"}, format='json')
=======
        req = RequestFactory().post('/events/updates')
        req.data = {'coreid':'testID',
                    'data':'{name:\'EventName\', code:\'1\', priority:\'1\'}'}
>>>>>>> 649d702bc4e7682875cedabee480eea5acb26419
        resp = views.CreateEventView.as_view()(req)
        assert resp.status_code == 404, 'Should throw 404 if not found'
