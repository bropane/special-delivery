"""Defines the models for handling device hardware information"""

from __future__ import unicode_literals
import random
import string

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Device(models.Model):
    """Stores the device information in DB"""
    name = models.CharField(max_length=20, blank=True, null=True)
    # Hardware Device ID
    device_id = models.CharField(max_length=25, null=False, unique=True)
    # Owners are always subscribed
    owner = models.ForeignKey(User, related_name='owner')
    # People who will receive email updates
    subscribers = models.ManyToManyField(User, related_name='subscribers')

    def __str__(self):
        if self.name and not self.name.isspace():
            return self.name
        else:
            return self.device_id


class DevicesKey(models.Model):
    """Key that is compiled with owner's devices to identify ownership.
       Similar to API key"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=30, unique=True, blank=True)

    # This gets called via a receiver when a User is saved
    @staticmethod
    def generate_device_key():
        key = ''.join(random.SystemRandom().choice(
            string.ascii_uppercase + string.digits) for _ in range(30))
        return key


@receiver(post_save, sender=User)
def create_devices_key(sender, instance, created, **kwargs):
    if created:
        DevicesKey.objects.create(user=instance,
                                  key=DevicesKey.generate_device_key)
