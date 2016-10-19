import pytest

from mixer.backend.django import mixer

from device_manager.models import Device

from ..models import Event


pytestmark = pytest.mark.django_db


class TestEvent:

    def test_init(self):
        device = mixer.blend(Device)
        event = mixer.blend(Event, device=mixer.SELECT)
        assert event.pk == 1, "Should create instance of Event"

    def test_ordering(self):
        device = mixer.blend(Device)
        events = mixer.cycle(100).blend(Event, device=mixer.SELECT)
        ordered_events = Event.objects.all()
        time1 = ordered_events[0].timestamp
        time2 = ordered_events[len(ordered_events)-1].timestamp
        assert time1 > time2, "Should order events from newest first"
