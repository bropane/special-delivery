from __future__ import unicode_literals
import os

from django.db import models
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import post_save

from device_manager.models import Device
from mailer.mailer import Mailer
from mailer.tests.fake_mailer import FakeMailer


class Event(models.Model):
    # 1: Status Update, 2: Movement Detected, 3: Config Change
    device = models.ForeignKey(Device)
    name = models.CharField(max_length=20, null=True)
    value = models.CharField(max_length=10, null=True, blank=True)
    code = models.IntegerField(default=0)
    priority = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=now, blank=True)

    class Meta:
        ordering = ('-timestamp',)

@receiver(post_save, sender=Event)
def send_notifications(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.priority > 2:
            device = instance.device
            receiver = device.owner.email
            subject = 'Device: {} | Event {}'.format(device.name, instance.name)
            body = "Value {}".format(instance.code)
            if os.getenv('MAILING', False):
                mailer = Mailer()
            else:
                mailer = FakeMailer()
                print "Using Fake Mailer"
            return mailer.mail(device, receiver, subject, body)
