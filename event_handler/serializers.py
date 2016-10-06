from rest_framework import serializers

from models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'device_id', 'type', 'battery', 'timestamp')
