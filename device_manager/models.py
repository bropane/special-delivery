"""Defines the models for handling device hardware information"""

from __future__ import unicode_literals
import random
import string

from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
