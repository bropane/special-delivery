from __future__ import unicode_literals
import random
import string

from django.contrib.auth.models import User
from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    # Hardware Device ID
    device_id = models.CharField(max_length=25, null=False, unique=True)
    # Owners are always subscribed
    owner = models.ForeignKey(User, related_name='owner')
    # People who will receive email updates
    subscribers = models.ManyToManyField(User, related_name='subscribers')
    # Auto-generated key to be compiled with device that idents. ownership
    device_key = models.CharField(max_length=30, unique=True, blank=True)

    def generate_device_key(self):
        key = ''.join(random.SystemRandom().choice(
            string.ascii_uppercase + string.digits) for _ in range(30))
        return key

    def save(self, *args, **kwargs):
        if not self.device_key:
            self.device_key = self.generate_device_key()
        super(Device, self).save(*args, **kwargs)

    def __str__(self):
        if self.name and not self.name.isspace():
            return self.name
        else:
            return self.device_id
