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
        device_id = request.data['device']
        try:
            device = Device.objects.get(device_id=device_id)
            if device.owner != request.user:
                raise PermissionDenied
            return self.create(request)
        except Device.DoesNotExist:
            raise Http404
