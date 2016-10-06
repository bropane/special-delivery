from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


class Location(models.Model):
    gps_location = models.CharField(max_length=30)
    device_id = models.CharField(max_length=25)
    timestamp = models.DateTimeField(default=now, blank=True)

    class Meta:
        ordering = ('-timestamp',)
