from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Location:
    gps_location = models.CharField(max_length=15)
    timestamp = models.DateTimeField()
    device_id = models.CharField(max_length=25)
