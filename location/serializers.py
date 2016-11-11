from rest_framework import serializers
from geoposition import Geoposition

from device_manager.models import Device

from models import Location


class LocationSerializer(serializers.ModelSerializer):

    device = serializers.SlugRelatedField(many=False,
                                          queryset=Device.objects.all(),
                                          slug_field='device_id')

    def create(self, validated_data):
        device = validated_data.pop('device', None)
        return Location.objects.create(device=device,
                                       **validated_data)

    class Meta:
        model = Location
        fields = ('id', 'position', 'device')
