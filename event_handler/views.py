import json

from django.http import Http404

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from device_manager.models import Device

from models import Event
from serializers import EventSerializer


class CreateEventView(CreateAPIView):
    """
    View to receive events from hardware and add to DB

    *Requires device_id
    """
    serializer_class = EventSerializer

    def post(self, request):
        device_id = request.data['coreid']
        data = json.loads(request.data['data'])
        try:
            device = Device.objects.get(device_id=device_id)
        except Device.DoesNotExist:
            raise Http404
        return Response(data)
