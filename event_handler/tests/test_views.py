import pytest

from django.test import RequestFactory
from mixer.backend.django import mixer

from .. import views

pytestmark = pytest.mark.django_db

class TestCreateEventView:

    def test_post(self):
        req = RequestFactory().post()
        resp = views.CreateEventView.as_view()(req)
        assert resp.status_code == 200
