import pytest
import json

from mixer.backend.django import mixer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from ..serializers import EventSerializer

pytestmark = pytest.mark.django_db


class TestEventSerializer:

    @pytest.fixture
    def user(self):
        from django.contrib.auth.models import User
        return mixer.blend(User)

    @pytest.fixture
    def device(self, user):
        from device_manager.models import Device
        return Device.objects.create(owner=user,
                                     device_id='testID',
                                     name="Test")

    @pytest.fixture
    def event(self, device):
        from ..models import Event
        return mixer.blend(Event, device=device)

    def test_encode(self, event):
        serializer = EventSerializer(event)
        jsonString = JSONRenderer().render(serializer.data)
        assert json.loads(jsonString)

    def test_decode(self, user, device):
        json = "{\"device\":\"testID\",\"priority\":\"2\",\"code\":\"1\", \
                \"value\":\"30\",\"name\":\"Armed\"}"
        stream = BytesIO(json)
        data = JSONParser().parse(stream)
        serializer = EventSerializer(data=data)
        assert serializer.is_valid(), 'Should deserialize properly to dict'
        event = serializer.save()
        assert event.pk, 'Should save an event from JSON'
