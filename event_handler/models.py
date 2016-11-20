from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

from device_manager.models import Device


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
            subject = str.format("Event: {0}", str(device),
                                 instance.name)
            body = str.format("Value: {0}", instance.code)
            mailer = FakeMailer()
            mailer.mail(device, receiver, subject, body)
            assert mailer.has_mailed() == True, 'Should try and send mail'
