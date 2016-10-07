from rest_framework.views import CreateAPIView
from rest_framework.response import Response

from device_manager.models import Device

from models import Event
from serializers import EventSerializer


class CreateEvent(CreateAPIView):
    """
    View to receive events from hardware and add to DB

    *Requires device_id
    """

    def post(self, request, format=None):
        device_id = request.data
        device = Device.objects.get(device_id=device_id)
        event = Event(device=device, type=request.type,
                      battery=request.battery)
        event.save()
        return Response()
