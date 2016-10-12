import pytest

from django.test import RequestFactory
from mixer.backend.django import mixer

from .. import views

pytestmark = pytest.mark.django_db

class TestCreateEventView:

    def test_post(self):
        req = RequestFactory().post('/events/updates')
        req.data = {'coreid':'testID',
                    'data':'{name:\'EventName\', code:\'1\', priority:\'1\'}'}
        resp = views.CreateEventView.as_view()(req)
        assert resp.status_code == 200
