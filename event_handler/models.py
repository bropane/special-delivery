from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event
    # 1: Status Update, 2: Movement Detected, 3: Config Change
    type = models.IntegerField()
    timestamp = models.DateTimeField()
    battery = models.CharField(max_length=12)
