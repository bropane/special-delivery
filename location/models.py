from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

from device_manager.models import Device


class Location(models.Model):
    gps_location = models.CharField(max_length=30)
    device = models.ForeignKey(Device)
    timestamp = models.DateTimeField(default=now, blank=True)

    class Meta:
        ordering = ('-timestamp',)
