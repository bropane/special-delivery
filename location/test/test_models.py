from geopostion import Geoposition
from mixer.backend.django import mixer

from device_manager.models import Device
from .models import Location


class TestModels:
    def test_create(self):
        device = mixer.blend(Device)
        loc = Location(position=point, de)
