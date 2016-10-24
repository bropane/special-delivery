import pytest

from mixer.backend.django import mixer
from geoposition import Geoposition

from device_manager.models import Device

from ..models import Location


pytestmark = pytest.mark.django_db


class TestLocation:

    def test_init(self):
        device = mixer.blend(Device)
        pos = Geoposition(52.3, -101.6)
        loc = Location(position=pos, device=device)
        loc.save()
        assert loc.pk == 1, "Should create instance of Event"

    def test_ordering(self):
        device = mixer.blend(Device)
        for i in range(0, 100):
            pos = Geoposition(43.4, -123.45346)
            loc = Location(position=pos, device=device)
            loc.save()
        ordered_events = Location.objects.all()
        time1 = ordered_events[0].timestamp
        time2 = ordered_events[len(ordered_events)-1].timestamp
        assert time1 > time2, "Should order events from newest first"
