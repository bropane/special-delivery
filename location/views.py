from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from models import Location
from serializers import LocationSerializer


class UpdateLocationView(CreateAPIView):
    queryset = Location
    serializer_class = LocationSerializer

    def post(self, request):
        pass
