import json

from rest_framework.generics import CreateAPIView
from django.http import Http404
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from geoposition import Geoposition

from device_manager.models import Device

from models import Location
from serializers import LocationSerializer


class UpdateLocationView(CreateAPIView):
    serializer_class = LocationSerializer

    def post(self, request):
        device_id = request.data['coreid']
        try:
            device = Device.objects.get(device_id=device_id)
            if device.owner != request.user:
                raise PermissionDenied
            data = json.loads(request.data['data'])
            position = data['position'].split(',')
            latitude = position[0]
            longitude = position[1]
            position = Geoposition(latitude=latitude, longitude=longitude)
            location = Location(position=position, device=device)
            location.save()
        except Device.DoesNotExist:
            raise Http404
        return Response(LocationSerializer(location).data)
