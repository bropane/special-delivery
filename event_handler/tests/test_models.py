import os
import pytest

from django.db.models.signals import post_save
from mixer.backend.django import mixer

from device_manager.models import Device
from mailer.mailer import Mailer
from mailer.tests.fake_mailer import FakeMailer

from ..models import Event


pytestmark = pytest.mark.django_db


class TestEvent:

    def test_init(self):
        device = mixer.blend(Device)
        event = mixer.blend(Event, device=mixer.SELECT)
        assert event.pk == 1, "Should create instance of Event"

    # def test_ordering(self):
    #     device = mixer.blend(Device)
    #     events = mixer.cycle(100).blend(Event, device=mixer.SELECT)
    #     ordered_events = Event.objects.all()
    #     time1 = ordered_events[0].timestamp
    #     time2 = ordered_events[len(ordered_events)-1].timestamp
    #     assert time1 > time2, "Should order events from newest first"

    def test_notification(self):
        device = mixer.blend(Device)
        event = Event(device=device, name='Test Event', priority=3)
        event.save()
        device = event.device
        receiver = device.owner.email
        subject = 'Device: {} | Event {}'.format(device.name, event.name)
        body = "Value {}".format(event.code)
        if os.getenv('MAILING', False):
            mailer = Mailer
        else:
            mailer = FakeMailer()
            print "Using Fake Mailer"
        resp = mailer.mail(device, receiver, subject, body)
        assert resp, 'Should try to send mail'
