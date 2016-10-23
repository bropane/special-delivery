import pytest

from mixer.backend.django import mixer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from ..serializers import EventSerializer

pytestmark = pytest.mark.django_db


class TestEventSerializer:

    def test_serializer(self):
        event = mixer.blend('event_handler.Event')
        json = JSONRenderer().render(EventSerializer(event).data)
        assert json, 'Should serialize Event to JSON'
        stream = BytesIO(str(json))
        data = JSONParser().parse(stream)
        serializer = EventSerializer(data=data)
        assert serializer.is_valid(), 'Should deserialize properly to dict'
