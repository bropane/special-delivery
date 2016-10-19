import pytest

from django.contrib.auth.models import User

from mixer.backend.django import mixer

from .. import models


pytestmark = pytest.mark.django_db

class TestDevice:

    def test_init(self):
        obj = mixer.blend('device_manager.Device')
        assert obj.pk == 1, 'Should save an instance'

    def test_str(self):
        obj = mixer.blend('device_manager.Device')
        assert obj.device_id == str(obj), 'Fail over to device_id if no name'
        obj.name = 'TD'
        assert obj.name == str(obj), 'Should give device name if present'
