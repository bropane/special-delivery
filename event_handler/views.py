import json

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

    def post(self, request):
        device_id = request.data['coreid']
        data = json.loads(request.data['data'])
        device = Device.objects.get(device_id=device_id)
        event = Event(device=device, type=1,
                      battery='test')
        event.save()
        return Response(request.data)
