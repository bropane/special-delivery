from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

from geoposition.fields import GeopositionField

from device_manager.models import Device


class Location(models.Model):
    position = GeopositionField()
    device = models.ForeignKey(Device)
    timestamp = models.DateTimeField(default=now, blank=True)

    class Meta:
        ordering = ('-timestamp',)
