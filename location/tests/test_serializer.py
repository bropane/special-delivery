import pytest

from mixer.backend.django import mixer
from geoposition import Geoposition
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from device_manager.models import Device

from ..models import Location
from ..serializers import LocationSerializer


pytestmark = pytest.mark.django_db


class TestSerializer:

    def test_serializer(self):
        device = mixer.blend(Device)
        pos = Geoposition(32.556, -122.45677)
        loc = Location(device=device, position=pos)
        loc.save()
        json = JSONRenderer().render(LocationSerializer(loc).data)
        assert json, 'Should serialize Location to JSON'
        stream = BytesIO(str(json))
        data = JSONParser().parse(stream)
        serializer = LocationSerializer(data=data)
        assert serializer.is_valid(), 'Should deserialize properly to dict'
