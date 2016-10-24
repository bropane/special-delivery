import json
import pytest

from mixer.backend.django import mixer
from rest_framework.test import APIRequestFactory


from ..views import UpdateLocationView

pytestmark = pytest.mark.django_db


class TestUpdateLocation:

    def test_post(self):
        data = json.dumps({"position": "33.45673,-133.52858"})
        req = APIRequestFactory().post('/location/update', {"data": data, "coreid": "testID", "name": "COORD"}, format='json')
        resp = UpdateLocationView.as_view()(req)
        assert resp.status_code == 404, 'Should throw 404 if not found'
