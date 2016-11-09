from rest_framework import serializers

from device_manager.models import Device

from models import Event


class EventSerializer(serializers.ModelSerializer):

    device = serializers.SlugRelatedField(many=False,
                                          queryset=Device.objects.all(),
                                          slug_field='device_id')

    def create(self, validated_data):
        device = validated_data.pop('device', None)
        return Event.objects.create(device=device, **validated_data)

    class Meta:
        model = Event
        fields = ('device', 'name', 'value',
                  'code', 'priority')
