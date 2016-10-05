from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


class Event(models.Model):
    # 1: Status Update, 2: Movement Detected, 3: Config Change
    type = models.IntegerField()
    battery = models.CharField(max_length=12)
    timestamp = models.DateTimeField(default=now, blank=True)
