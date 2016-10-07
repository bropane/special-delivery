from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

from device_manager.models import Device


class Event(models.Model):
    # 1: Status Update, 2: Movement Detected, 3: Config Change
    device = models.ForeignKey(Device)
    type = models.IntegerField()
    battery = models.CharField(max_length=12)
    timestamp = models.DateTimeField(default=now, blank=True)

    class Meta:
        ordering = ('-timestamp',)
